import tkinter as tk
import functools
from eventListeners.screenActions import *

def buttonCreateListener(mainScreen, buttonCreateLog):
    screenFormCreateLog = tk.Toplevel(mainScreen)
    screenFormCreateLog.focus_set()
    buttonCreateLog["state"] = "disabled"

    #SpLog-CreateScreen ... do form

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
