import tkinter as tk
import os
import sys
import functools
from eventListeners.buttonListeners import *

def setPositionOfElementsInFrame(dictParams):
    if dictParams['positionFrame'] == 'top':
        #set all elements in frame top
        labelInfoTop = tk.Label(master=dictParams['frame'], text="Sistema de control de rutina esportiva. Aquí podràs veure els logs que insertis")
        labelInfoTop.pack(padx=5, pady=20)
        buttonCreate = generateCreateButton({
            'frame': dictParams['frame'],
            'screen': dictParams['screen']
        })
        buttonCreate.pack(padx=5, pady=5, side=tk.TOP)
    
    elif dictParams['positionFrame'] == 'bottom':
        label_b = tk.Label(master=dictParams['frame'], text="I'm Frame of logs")
        label_b.pack()

def getProgramIcon():
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if "logoLogsSport.ico" in files:
            return os.path.join(root, "logoLogsSport.ico")
    return ""

def generateCreateButton(configParams):
    buttonCreate = tk.Button(master = configParams['frame'], command = functools.partial(buttonCreateListener,configParams['screen']), text="Crear Log")
    return buttonCreate


def generateFrames(screen):
    frame_buttons = tk.Frame(master=screen, height=100)
    frame_logs = tk.Frame(master=screen, height=477)

    return {'frameButtons':frame_buttons, 'frameLogs':frame_logs}

def setWindowAttributes():
    root = tk.Tk()
    root.geometry("900x500")
    root.minsize(500, 200)
    programIcon = getProgramIcon()
    if programIcon:
        root.iconbitmap(programIcon)
    root.winfo_toplevel().title("Sport log -- CONTROL DE LA RUTINA D'ESPORT")
    return root

def executeScreen(tkScreen):
    tkScreen.mainloop()

def packFrames(elementsToShow):
    for elementName, elementToPack in elementsToShow.items():
        elementToPack.pack(fill=tk.BOTH, side=tk.TOP, expand=True)