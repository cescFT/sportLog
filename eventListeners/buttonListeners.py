import os
import sys
import tkinter as tk
import functools
from eventListeners.screenActions import *

def getIconOfSpecificScreen(screenName):
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if screenName == 'createLogScreen' and "plus.ico" in files:
            return os.path.join(root, "plus.ico")
    return ""

def buttonCreateLogListener(mainScreen, buttonCreateLog):
    screenFormCreateLog = tk.Toplevel(mainScreen)
    screenFormCreateLog.geometry("600x400")
    screenFormCreateLog.minsize(200, 200)
    screenIcon = getIconOfSpecificScreen('createLogScreen')
    if screenIcon:
        screenFormCreateLog.iconbitmap(screenIcon)
    screenFormCreateLog.winfo_toplevel().title("Sport log - CREAR LOG")
    screenFormCreateLog.focus_set()
    buttonCreateLog["state"] = "disabled"
    #TODO
    #frameForm = 

    screenFormCreateLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateLogForm, screenFormCreateLog, buttonCreateLog))

def buttonEditLogListener(mainScreen, buttonEditLog, treeView):
    screenEditLog = tk.Toplevel(mainScreen)
    screenEditLog.focus_set()
    buttonEditLog['state'] = 'disabled'

    #SpLog-CreateScreen ... do screen
    for i in treeView.selection():
        print("you clicked on", treeView.item(i))

    screenEditLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseEditLog, screenEditLog, buttonEditLog))


def buttonDeleteLogListener(mainScreen, buttonDeleteLog, treeView):
    screenDeleteLog = tk.Toplevel(mainScreen)
    screenDeleteLog.focus_set()
    buttonDeleteLog['state'] = 'disabled'

    screenDeleteLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseDeleteLog, screenDeleteLog, buttonDeleteLog))

def buttonCreateReminderListener(mainScreen, buttonCreateReminder):
    screenCreateReminders = tk.Toplevel(mainScreen)
    screenCreateReminders.focus_set()
    buttonCreateReminder['state'] = 'disabled'
    #SpLog-CreateScreen ... do form

    screenCreateReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateReminder, screenCreateReminders, buttonCreateReminder))

def buttonStatisticsListener(mainScreen, buttonStatistics):
    screenStatistics = tk.Toplevel(mainScreen)
    screenStatistics.focus_set()
    buttonStatistics['state'] = 'disabled'
    #SpLog-CreateScreen ... do screen

    screenStatistics.protocol("WM_DELETE_WINDOW", functools.partial(onCloseStatistics, screenStatistics, buttonStatistics))

def buttonListRemindersListener(mainScreen, buttonListReminders):
    screenListReminders = tk.Toplevel(mainScreen)
    screenListReminders.focus_set()
    buttonListReminders['state'] = 'disabled'
    #SpLog-CreateScreen ... do list

    screenListReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseListReminders, screenListReminders, buttonListReminders))
