import os
import sys
import tkinter as tk
import functools
from tkinter import ttk
from eventListeners.screenActions import *
from logsManager.sportLogManager import *
from tkcalendar import Calendar, DateEntry
import datetime

def getDurationHour(hourPicker):
    print(hourPicker.get())

def getValueSelectedDifficulty(dropdownDifficulty):
    print(dropdownDifficulty.get())

def getValueSelectedSport(dropdownSport):
    print(dropdownSport.get())

def selectData(root, labelSportDaySelected):
    def print_sel():
        print(labelSportDaySelected)
        labelSportDaySelected['text'] = cal.selection_get()
        datepickerScreen.destroy()

    datepickerScreen = tk.Toplevel(root)
    datepickerScreen.winfo_toplevel().title("Sport log - SELECCIONA DATA")
    screenCalendarIcon = getIconOfSpecificScreen('selectData')
    if screenCalendarIcon:
        datepickerScreen.iconbitmap(screenCalendarIcon)
    datepickerScreen.focus_set()
    datepickerScreen.geometry("700x500")

    cal = Calendar(datepickerScreen,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
    cal.pack(fill="both", expand=True)
    ttk.Button(datepickerScreen, text="Desar Data", command=print_sel).pack()

def getIconOfSpecificScreen(screenName):
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if screenName == 'createLogScreen' and "plus.ico" in files:
            return os.path.join(root, "plus.ico")
        elif screenName == 'selectData' and "calendar.ico" in files:
            return os.path.join(root, "calendar.ico")
        elif screenName == 'editLogScreen' and "edit.ico" in files:
            return os.path.join(root, "edit.ico")
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
    #CREATING FORM TO NEW LOG
    
    # 1-Sport dropdown
    sportOptions = [
        'esport 1',
        'esport 2',
        'esport 3'
    ]
    frameSportSelect = tk.Frame(screenFormCreateLog)
    labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
    dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
    dropdownSport['values'] = sportOptions
    dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport))
    dropdownSport.grid(row=0, column=1)
    frameSportSelect.pack(side=tk.TOP)

    # 2-SportDay
    frameSportDay = tk.Frame(screenFormCreateLog)
    labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
    labelSportDaySelected = tk.Label(
        frameSportDay,
        text="{}".format(datetime.datetime.now().strftime("%Y-%m-%d"))
    )
    labelSportDaySelected.grid(row=0, column=1)

    dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
    dadepickerButton['command'] = functools.partial(selectData, screenFormCreateLog, labelSportDaySelected)
    dadepickerButton.grid(row=0, column=2)

    frameSportDay.pack(side=tk.TOP)

    # 3- Duration
    frameDuration = tk.Frame(screenFormCreateLog)
    labelTimeElapsed = tk.Label(frameDuration, text = "Durada (h,m,s)").grid(row=0, column=0, padx=4, pady=10)
    hourPicker = ttk.Spinbox(frameDuration, from_=1, to=23, wrap=True, width=5, state="readonly")
    hourPicker['command'] = functools.partial(getDurationHour,hourPicker)
    hourPicker.grid(row=0, column=1)
    tk.Label(frameDuration, text="h").grid(row=0,column=2)
    minutePicker = ttk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly").grid(row=0, column=3)
    tk.Label(frameDuration, text="m").grid(row=0, column=4)
    secondsPicker = ttk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly").grid(row=0, column=5)
    tk.Label(frameDuration, text="s").grid(row=0,column=6)

    frameDuration.pack(side=tk.TOP)
    
    # 4- Difficculty
    frameDifficulty = tk.Frame(screenFormCreateLog)
    labelDificulty = tk.Label(frameDifficulty ,text = "Dificultat").grid(row=0, column=0, padx=4, pady=10)

    difficultyOptions = [
        '1-Molt fàcil',
        '2-Fàcil',
        '3-Mitjà',
        '4-Mitjà alt',
        '5-Difícil',
        '6-Extremadament difícil'
    ]

    dropdownDifficulty = ttk.Combobox(frameDifficulty, state="readonly")
    dropdownDifficulty['values'] = difficultyOptions
    dropdownDifficulty.bind('<<ComboboxSelected>>', lambda event: getValueSelectedDifficulty(dropdownDifficulty))
    dropdownDifficulty.grid(row=0, column=1)
    frameDifficulty.pack(side=tk.TOP)

    #Submit button new log
    frameButtonSubmitNewLog = tk.Frame(screenFormCreateLog)
    buttonSubmitNewLog = ttk.Button(frameButtonSubmitNewLog, text="Desar nou log")
    buttonSubmitNewLog['command'] = functools.partial(saveNewSportLog )
    buttonSubmitNewLog.pack(padx=50, pady=50)
    frameButtonSubmitNewLog.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    

    screenFormCreateLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateLogForm, screenFormCreateLog, buttonCreateLog))

def buttonEditLogListener(mainScreen, buttonEditLog, treeView):
    screenEditLog = tk.Toplevel(mainScreen)
    screenEditLog.geometry("600x400")
    screenEditLog.minsize(200, 200)
    screenEditLogIcon = getIconOfSpecificScreen('editLogScreen')
    if screenEditLogIcon:
        screenEditLog.iconbitmap(screenEditLogIcon)
    screenEditLog.winfo_toplevel().title("Sport log - EDITAR LOG(s) SELECCIONATS")
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
