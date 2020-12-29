from logsManager.dbConnection import *
import tkinter as tk
import datetime

def deleteOldReminders(pastMonday, pastSunday):
    save('DELETE FROM recordatori WHERE date(dia) BETWEEN  date(\''+pastMonday.strftime("%Y-%m-%d")+'\') AND date(\''+pastSunday.strftime("%Y-%m-%d")+'\')')

def getAllReminders(actualMonday, actualSunday):
    return execute('SELECT r.dia, e.nom_esport FROM recordatori r INNER JOIN esport e ON r.esport = e.id WHERE date(dia) BETWEEN  date(\''+actualMonday.strftime("%Y-%m-%d")+'\') AND date(\''+actualSunday.strftime("%Y-%m-%d")+'\')')

def saveReminder(infoToSave, buttonCreateReminder, screenCreateReminders, textboxHour):
    if len(infoToSave.keys()) == 2 and textboxHour.get():
        try:
            hour = int(textboxHour.get().split(":")[0])
            minutes = int(textboxHour.get().split(":")[1])
        except Exception:
            tk.messagebox.showerror(title="Error en la hora", message="El camp ha d'estar ple seguit el format hh:mm. Per exemple, 10:30.")
            screenCreateReminders.wm_attributes("-topmost", 1)
            screenCreateReminders.focus_force()
            return
        sportId = execute('SELECT id FROM esport WHERE nom_esport LIKE "%'+infoToSave['sport']+'%"')[0][0]
        if infoToSave['date'] <= datetime.datetime.now().date():
            tk.messagebox.showerror(title="Error en el recordatori", message="La data posada com a recordatori ha de ser major a avui!")
            screenCreateReminders.wm_attributes("-topmost", 1)
            screenCreateReminders.focus_force()
        else:
            dateSport = datetime.datetime(infoToSave['date'].year, infoToSave['date'].month, infoToSave['date'].day, hour, minutes).strftime("%Y-%m-%d %H:%M:%S")
            try:
                save('INSERT INTO recordatori (dia, esport) VALUES (\''+dateSport+'\','+str(sportId)+')')
                tk.messagebox.showinfo(title="Guardat", message="S'ha desat el nou recordatori correctament!")
            except Exception:
                tk.messagebox.showerror(title="Error al desar", message="S'ha interromput la comunicació amb la base de dades")
            
            buttonCreateReminder['state'] = 'normal'
            screenCreateReminders.destroy()
    else:
        keys = [
            'date',
            'sport'
        ]
        sToPut = "Falten camps per a completar. Falten:\n"
        for key in keys:
            if key not in infoToSave:
                sToPut += "* "+key + "\n"
        if not textboxHour.get():
            sToPut+= "* hora \n"
        tk.messagebox.showerror(title="Error al desar", message=sToPut)
        screenCreateReminders.wm_attributes("-topmost", 1)
        screenCreateReminders.focus_force()