import tkinter as tk
from screenCreate.screenComponents import *

def generateWindow():
    root = setWindowAttributes()
    frames = generateFrames()

    # set buttons

    label_a = tk.Label(master=frames['frameButtons'], text="I'm Frame of buttons")
    label_a.pack()

    label_b = tk.Label(master=frames['frameLogs'], text="I'm Frame of logs")
    label_b.pack()

    packElements({
        'frameButtons' : frames['frameButtons'],
        'frameLogs' : frames['frameLogs']
    })
    
    executeScreen(root)


if __name__ == "__main__":
    generateWindow()