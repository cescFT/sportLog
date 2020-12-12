import tkinter as tk
from tkinter import messagebox

def onCloseCreateLogForm(screenFormCreateLog, buttonCreateLog):
    buttonCreateLog['state'] = 'normal'
    screenFormCreateLog.destroy()

def onCloseListReminders(screenListReminders, buttonListReminders):
    buttonListReminders['state'] = 'normal'
    screenListReminders.destroy()

def onCloseCreateReminder(screenReminder, buttonCreateReminder):
    buttonCreateReminder['state'] = 'normal'
    screenReminder.destroy()

def onCloseStatistics(screenStatistics, buttonStatistics):
    buttonStatistics['state'] = 'normal'
    screenStatistics.destroy()

def onCloseEditLog(screenEditLog, buttonEditLog):
    buttonEditLog['state'] = 'normal'
    screenEditLog.destroy()
