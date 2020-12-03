import tkinter as tk
import os
import sys

def getProgramIcon():
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if "logoLogsSport.ico" in files:
            return os.path.join(root, "logoLogsSport.ico")
    return ""

def generateCreateButton():
    pass

def generateFrames():
    frame_buttons = tk.Frame()
    frame_logs = tk.Frame()

    return {'frameButtons':frame_buttons, 'frameLogs':frame_logs}

def setWindowAttributes():
    root = tk.Tk()
    root.geometry("800x500")
    programIcon = getProgramIcon()
    if programIcon:
        root.iconbitmap(programIcon)
    root.winfo_toplevel().title("Sport log -- CONTROL DE LA RUTINA D'ESPORT")
    return root

def executeScreen(tkScreen):
    tkScreen.mainloop()

def packElements(elementsToShow):
    if elementsToShow:
        for elementName, elementToPack in elementsToShow.items():
            elementToPack.pack()
    
        return True
    else:
        return False