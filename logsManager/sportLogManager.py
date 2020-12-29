from logsManager.dbConnection import *
import tkinter as tk

def updateValuesTreeView(treeView):
    sportLogs = execute("SELECT e.id, sp.nom_esport, e.durada, e.dia_esport, d.dificultat FROM esport_log e INNER JOIN esport sp ON sp.id = e.esport INNER JOIN dificultat d ON d.id = e.dificultat ORDER BY e.dia_esport DESC")
    
    for elementTreeView in treeView.get_children():
            treeView.delete(elementTreeView)
        
    for spLog in sportLogs:
        treeView.insert("", spLog[0], text="Log {}".format(spLog[0]), values=(spLog[1],spLog[2].split(":")[0]+" h:"+spLog[2].split(":")[1]+" m:"+spLog[2].split(":")[2]+" s",spLog[3].strftime("%d-%m-%Y"), spLog[4]))

def saveNewSportLog(infoToSave, screenFormCreateLog, buttonCreateLog, treeView):
    if len(infoToSave.keys()) == 6:
        sportId = execute('SELECT id FROM esport WHERE nom_esport LIKE "%'+infoToSave['sport']+'%"')[0][0]
        dateSport = infoToSave['date'].strftime("%Y-%m-%d")
        duration = infoToSave['hora']+":"+infoToSave['minuts']+":"+infoToSave['segons']
        difficulty = infoToSave['dificultat'].replace("{", "").replace("}", "")
        difficultyId = execute("SELECT id FROM dificultat WHERE dificultat LIKE '%"+difficulty+"%'")[0][0]
        try:
            save('INSERT INTO esport_log (dia_esport, durada, esport, dificultat) VALUES (\''+dateSport+'\', \''+duration+'\', '+str(sportId)+' ,'+str(difficultyId)+')')
            tk.messagebox.showinfo(title="Guardat", message="S'ha desat el nou log correctament!")
        except Exception:
            tk.messagebox.showerror(title="Error al desar", message="S'ha interromput la comunicació amb la base de dades")
        
        updateValuesTreeView(treeView)
        buttonCreateLog['state'] = 'normal'
        screenFormCreateLog.destroy()
    else:
        keys = [
            'sport',
            'date',
            'hora',
            'minuts',
            'segons',
            'dificultat'
        ]
        sToPut = "Falten camps per a completar. Falten:\n"
        for key in keys:
            if key not in infoToSave:
                sToPut += "* "+key + "\n"
        tk.messagebox.showerror(title="Error al desar", message=sToPut)
        screenFormCreateLog.wm_attributes("-topmost", 1)
        screenFormCreateLog.focus_force()


def editSportLog(infoToSave, treeView, screenEditLog):
    sportId = execute('SELECT id FROM esport WHERE nom_esport LIKE "%'+infoToSave['sport']+'%"')[0][0]
    difficulty = infoToSave['dificultat'].replace("{", "").replace("}", "")
    difficultyId = execute("SELECT id FROM dificultat WHERE dificultat LIKE '%"+difficulty+"%'")[0][0]
    duration = infoToSave['hora']+":"+infoToSave['minuts']+":"+infoToSave['segons']
    dateSport = infoToSave['date'].strftime("%Y-%m-%d")
    try:
        save('UPDATE esport_log SET dia_esport=\''+dateSport+'\', durada=\''+duration+'\', esport='+str(sportId)+', dificultat='+str(difficultyId)+' WHERE id='+infoToSave['id']+'')
        tk.messagebox.showinfo(title="Guardat", message="S'ha actualitzat el log correctament!")
        updateValuesTreeView(treeView)
        screenEditLog.wm_attributes("-topmost", 1)
        screenEditLog.focus_force()
    except Exception as ex:
        tk.messagebox.showerror(title="Error al actualitzar", message="S'ha interromput la comunicació amb la base de dades")

def deleteSportLog(infoToDelete):
    try:
        save('DELETE FROM esport_log WHERE id='+infoToDelete['text'].split(" ")[1])
    except Exception:
        tk.messagebox.showerror(title="Error al eliminar", message="S'ha interromput la comunicació amb la base de dades")