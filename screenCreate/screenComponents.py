import tkinter as tk
from tkinter import ttk
import os
import sys
import functools
from eventListeners.buttonListeners import *

def setPositionOfElementsInFrame(dictParams):
    if dictParams['positionFrame'] == 'top':
        frameButtons = tk.Frame(master=dictParams['frame'])
        labelInfoTop = tk.Label(master=dictParams['frame'], text="Sistema de control de rutina esportiva. Aquí podràs veure els logs que insertis")
        labelInfoTop.pack(padx=5, pady=20)

        buttonReminders = generateButtonReminders({
            'frame': frameButtons
        })
                
        buttonStatistics = generateStatisticsButton({
            'frame': frameButtons
        })
        
        buttonReminders.pack(padx=5, pady=5, side="left")
        buttonStatistics.pack(padx=5, pady=5, side="left")
        frameButtons.pack()
    
    elif dictParams['positionFrame'] == 'bottom':
        frameTree = tk.Frame(master=dictParams['frame'])
        frameButtonsLogActions = tk.Frame(master=dictParams['frame'])
        labelInfoDB = tk.Label(master=dictParams['frame'], text="Accions log:")
        labelInfoDB.pack()

        buttonCreate = generateCreateButton({
            'frame': frameButtonsLogActions,
            'screen': dictParams['screen']
        })

        buttonEditLog = generateEditLogButton({
            'frame': frameButtonsLogActions
        })

        buttonDeleteLog = generateDeleteLogButton({
            'frame': frameButtonsLogActions
        })

        buttonCreate.pack(side="left", padx=5, pady=5)
        buttonEditLog.pack(side="left", padx=5, pady=5)
        buttonDeleteLog.pack(side="left", padx=5, pady=5)
        frameButtonsLogActions.pack()

        tree = ttk.Treeview(frameTree)
        tree["columns"] = ("C1", "C2", "C3", "C4")
        tree.column("#0", width=60, minwidth=60, stretch=tk.NO)
        tree.column("C1", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C2", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C3", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C4", width=200, minwidth=200, stretch=tk.NO)
        tree.heading("#0", text="ID", anchor=tk.W)
        tree.heading("C1", text="Esport", anchor=tk.W)
        tree.heading("C2", text="Durada", anchor=tk.W)
        tree.heading("C3", text="Dia esport", anchor=tk.W)
        tree.heading("C4", text="Dificultat", anchor=tk.W)

        
        for i in range(20):
            item = tree.insert("", i, text="Log {}".format(i), values=("esport","durada","diaesport", "dificultat"))
            if i == 0:
                tree.selection_set(item)
                tree.focus(item)
        vsb = ttk.Scrollbar(frameTree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        

        tree.pack(side="left", expand=True)
        vsb.pack(side='right', fill='y')
        frameTree.pack(padx=5, pady=5)
        

def getProgramIcon():
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if "logoLogsSport.ico" in files:
            return os.path.join(root, "logoLogsSport.ico")
    return ""

def generateButtonReminders(configParams):
    return tk.Button(master=configParams['frame'], text="Crear recordatori") #falta la crida a la funcio

def generateStatisticsButton(configParams):
    return tk.Button(master=configParams['frame'], text="Estadístiques") #falta la crida a la funcio

def generateEditLogButton(configParams):
    return tk.Button(master=configParams['frame'], text="Editar log") #falta la crida a la funcio

def generateDeleteLogButton(configParams):
    return tk.Button(master=configParams['frame'], text="Eliminar log") #falta la crida a la funcio

def generateCreateButton(configParams):
    return tk.Button(master = configParams['frame'], command = functools.partial(buttonCreateListener,configParams['screen']), text="Crear Log")

def generateFrames(screen):
    frame_buttons = tk.Frame(master=screen, height=100)
    frame_logs = tk.Frame(master=screen, height=477)

    return {'frameButtons':frame_buttons, 'frameLogs':frame_logs}

def setWindowAttributes():
    root = tk.Tk()
    root.geometry("1000x500")
    root.minsize(890, 400)
    programIcon = getProgramIcon()
    if programIcon:
        root.iconbitmap(programIcon)
    root.winfo_toplevel().title("Sport log - CONTROL DE LA RUTINA ESPORTIVA")
    return root

def executeScreen(tkScreen):
    tkScreen.mainloop()

def packFrames(elementsToShow):
    for elementName, elementToPack in elementsToShow.items():
        elementToPack.pack(fill=tk.BOTH, side=tk.TOP, expand=True)