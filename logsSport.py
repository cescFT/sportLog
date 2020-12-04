import tkinter as tk
from tkinter.ttk import *
from screenCreate.screenComponents import *

def generateWindow():
    root = setWindowAttributes()
    frames = generateFrames(root) 
    # afegir les coses bé dins de cada frame...
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
    generateWindow()