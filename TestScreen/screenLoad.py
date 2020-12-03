
from tkinter import Tk,Button,Frame #import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import time

starttime=time.time()

def loadbar(value):
    bar['value'] += value

def clicked():
    loadbar(5)

def tick_loadingbar(event):
    if event.widget == window:
        while(bar["value"] < 100):
            loadbar(25)
            time.sleep(1)

window = Tk()
window.title("Loading Bar app")
window.geometry('350x200')
window.bind("<Map>", tick_loadingbar)
style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background='lightgreen')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 25
bar.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=1)

window.mainloop()