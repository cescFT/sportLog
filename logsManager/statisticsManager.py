
import tkinter as tk
import numpy as np
import functools
from eventListeners.screenActions import onCloseStatistics
from logsManager.dbConnection import *

def statistics(screenStatisticsIcon, buttonStatistics):
    screenStatistics = tk.Tk()
    screenStatistics.wm_title("Sport log - ESTADÍSTIQUES")
    if screenStatisticsIcon:
        screenStatistics.iconbitmap(screenStatisticsIcon)
    screenStatistics.wm_attributes("-topmost", 1)
    screenStatistics.focus_force()
    screenStatistics.geometry("700x500")

    frameInfoBySport = tk.Frame(screenStatistics)
    tk.Label(screenStatistics, text="VEGADES REALITZADA CADA ACTIVITAT FÍSICA").pack(side=tk.TOP)
    sports = execute('SELECT id, nom_esport FROM esport')
    i=2
    for sport in sports:
        tk.Label(frameInfoBySport, text = sport[1]).grid(row=i, column=0)
        tk.Label(frameInfoBySport, text = str(execute('SELECT COUNT(*) FROM esport_log WHERE esport = '+str(sport[0]))[0][0])).grid(row=i, column=1)
        i= i + 1
    
    frameInfoBySport.pack(side=tk.TOP)
    tk.Label(screenStatistics, text="VEGADES REALITZADA CADA ACTIVITAT FÍSICA PER DIFICULTAT").pack(side=tk.TOP)
    frameInfoByDifficulty = tk.Frame(screenStatistics)
    difficulties = execute('SELECT id, dificultat FROM dificultat')
    i=2
    for difficulty in difficulties:
        tk.Label(frameInfoByDifficulty, text = difficulty[1]).grid(row=i, column=0)
        tk.Label(frameInfoByDifficulty, text = str(execute('SELECT COUNT(*) FROM esport_log WHERE dificultat = '+str(difficulty[0]))[0][0])).grid(row=i, column=1)
        i = i + 1
    frameInfoByDifficulty.pack(side=tk.TOP)
    screenStatistics.protocol("WM_DELETE_WINDOW", functools.partial(onCloseStatistics, screenStatistics, buttonStatistics))