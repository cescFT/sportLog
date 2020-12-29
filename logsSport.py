import tkinter as tk
from tkinter.ttk import *
from screenCreate.screenComponents import *
from logsManager.dbConnection import execute
from logsManager.reminderManager import getAllReminders, deleteOldReminders
from datetime import datetime, timedelta


def showAlerts():
    now = datetime.now()
    actualMonday = now - timedelta(days=now.weekday())
    actualSunday = actualMonday + timedelta(days=6)
    pastMonday = now - timedelta(days=now.weekday(), weeks=1)
    pastSunday = pastMonday + timedelta(days=6)
    deleteOldReminders(pastMonday, pastSunday)
    remindersCurrentWeek = getAllReminders(actualMonday, actualSunday)
    if remindersCurrentWeek:
        sToPut = ""
        for reminder in remindersCurrentWeek:
            sToPut+= "* "+reminder[0].strftime("%d-%m-%Y a les %H:%M:%S hores")+" -> "+reminder[1]
        sToPut+="\n\nPots veure aquesta informació a listar recordatoris.\nRecorda que els recordatoris són setmanals, és a dir, al acabar la setmana, s'eliminen automàticament."
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showinfo(title="Recordatoris setmanals", message=sToPut)
        root.destroy()


def generateWindow():
    root = setWindowAttributes()
    frames = generateFrames(root)

    setPositionOfElementsInFrame({
        'positionFrame': 'top',
        'frame': frames['frameButtons'],
        'screen': root
    })
    setPositionOfElementsInFrame({
        'positionFrame': 'bottom',
        'frame': frames['frameLogs'],
        'screen': root
    })

    packFrames({
        'frameButtons' : frames['frameButtons'],
        'frameLogs' : frames['frameLogs']
    })
    
    executeScreen(root)


if __name__ == "__main__":
    dbConnection = execute("SELECT VERSION()")
    if dbConnection:
        showAlerts()
        generateWindow()
    else:
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showerror(title="Connexió amb base de dades", message="No es pot establir comunicació amb base de dades")
        root.destroy()