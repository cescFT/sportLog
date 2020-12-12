import os
import sys
import tkinter as tk
import functools
from tkinter import ttk
from eventListeners.screenActions import *
from logsManager.sportLogManager import *
from logsManager.reminderManager import *
from logsManager.statisticsManager import *
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
        elif screenName == 'createReminder' or screenName == 'remindersList' and "reminder.ico" in files:
            return os.path.join(root, "reminder.ico")
        elif screenName == 'statisticsScreen' and "statistics.ico" in files:
            return os.path.join(root, "statistics.ico")
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
    if treeView.selection():
        screenEditLog = tk.Toplevel(mainScreen)
        screenEditLog.state('zoomed')
        screenEditLogIcon = getIconOfSpecificScreen('editLogScreen')
        if screenEditLogIcon:
            screenEditLog.iconbitmap(screenEditLogIcon)
        screenEditLog.winfo_toplevel().title("Sport log - EDITAR LOG(s) SELECCIONATS")
        screenEditLog.focus_set()
        buttonEditLog['state'] = 'disabled'

        sportOptions = [
            'esport 1',
            'esport 2',
            'esport 3',
            'esport'
        ]

        difficultyOptions = [
            '1-Molt fàcil',
            '2-Fàcil',
            '3-Mitjà',
            '4-Mitjà alt',
            '5-Difícil',
            '6-Extremadament difícil',
            'dificultat'
        ]

        mainFrameScreenEditLog = tk.Frame(screenEditLog)
        mainFrameScreenEditLog.pack(fill=tk.BOTH, expand=True)
        canvasEditLog = tk.Canvas(mainFrameScreenEditLog)
        canvasEditLog.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbarScreen = ttk.Scrollbar(mainFrameScreenEditLog, orient=tk.VERTICAL, command=canvasEditLog.yview)
        scrollbarScreen.pack(side=tk.RIGHT, fill=tk.Y)

        canvasEditLog.configure(yscrollcommand=scrollbarScreen.set)
        canvasEditLog.bind('<Configure>', lambda event: canvasEditLog.configure(scrollregion=canvasEditLog.bbox("all")))

        frameFormEditLog = tk.Frame(canvasEditLog)

        canvasEditLog.create_window((frameFormEditLog.winfo_screenwidth()/2,frameFormEditLog.winfo_screenwidth()/2), window=frameFormEditLog)
        
        
        for i in treeView.selection():
            print("you clicked on", treeView.item(i))
            frameFormEditLogForm = tk.Frame(frameFormEditLog, borderwidth=2, relief="groove")
            # 1-Sport dropdown
            frameSportSelect = tk.Frame(frameFormEditLogForm)
            labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
            dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
            dropdownSport['values'] = sportOptions
            dropdownSport.current(sportOptions.index(treeView.item(i)['values'][0]))
            dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport))
            dropdownSport.grid(row=0, column=1)
            frameSportSelect.pack(side=tk.TOP)
            
            # 2-SportDay
            frameSportDay = tk.Frame(frameFormEditLogForm)
            labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
            labelSportDaySelected = tk.Label(
                frameSportDay,
                text="{}".format(datetime.datetime.now().strftime("%Y-%m-%d")) # Modify with date getted of db
            )
            labelSportDaySelected.grid(row=0, column=1)

            dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
            dadepickerButton['command'] = functools.partial(selectData, screenEditLog, labelSportDaySelected)
            dadepickerButton.grid(row=0, column=2)
            frameSportDay.pack(side=tk.TOP)

            # 3- Duration
            frameDuration = tk.Frame(frameFormEditLogForm)
            labelTimeElapsed = tk.Label(frameDuration, text = "Durada (h,m,s)").grid(row=0, column=0, padx=4, pady=10)
            hourPicker = tk.Spinbox(frameDuration, from_=1, to=23, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=2)) # Modify with data of DB
            hourPicker['command'] = functools.partial(getDurationHour,hourPicker)
            hourPicker.grid(row=0, column=1)
            tk.Label(frameDuration, text="h").grid(row=0,column=2)
            minutePicker = tk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=2)).grid(row=0, column=3) # Modify with data of DB
            tk.Label(frameDuration, text="m").grid(row=0, column=4)
            secondsPicker = tk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=2)).grid(row=0, column=5) # Modify with data of DB
            tk.Label(frameDuration, text="s").grid(row=0,column=6)

            frameDuration.pack(side=tk.TOP)
            
            # 4- Difficculty
            frameDifficulty = tk.Frame(frameFormEditLogForm)
            labelDificulty = tk.Label(frameDifficulty ,text = "Dificultat").grid(row=0, column=0, padx=4, pady=10)

            dropdownDifficulty = ttk.Combobox(frameDifficulty, state="readonly")
            dropdownDifficulty['values'] = difficultyOptions
            dropdownDifficulty.bind('<<ComboboxSelected>>', lambda event: getValueSelectedDifficulty(dropdownDifficulty))
            dropdownDifficulty.current(difficultyOptions.index(treeView.item(i)['values'][3]))
            dropdownDifficulty.grid(row=0, column=1)
            frameDifficulty.pack(side=tk.TOP)

            #Submit button edit log
            frameButtonSubmitEditLog = tk.Frame(frameFormEditLogForm)
            buttonSubmitNewLog = ttk.Button(frameButtonSubmitEditLog, text="Editar log")
            buttonSubmitNewLog['command'] = functools.partial(editSportLog)
            buttonSubmitNewLog.pack(padx=50, pady=50)
            frameButtonSubmitEditLog.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
            
            frameFormEditLogForm.pack(padx=5, pady=10)      

        screenEditLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseEditLog, screenEditLog, buttonEditLog))
    else:
        tk.messagebox.showwarning(title="Editar log(s)", message="Selecciona almenys un dels logs mostrat en el llistat")


def buttonDeleteLogListener(treeView):
    if treeView.selection():
        result = tk.messagebox.askquestion("Eliminar Log (s)", "Prem Si per a eliminar, altrament No.", icon='question')
        if result == 'yes':
            for item in treeView.selection():
                infoToDeleteFromDB = treeView.item(item)
                deleteSportLog() # we need to pass info to delete
                treeView.delete(item)
    else:
        tk.messagebox.showwarning(title="Eliminar log(s)", message="Selecciona almenys un dels logs mostrat en el llistat per a eliminar-lo")

def buttonCreateReminderListener(mainScreen, buttonCreateReminder):
    screenCreateReminders = tk.Toplevel(mainScreen)
    buttonCreateReminder['state'] = 'disabled'
    screenCreateReminders.winfo_toplevel().title("Sport log - CREAR RECORDATORI")
    screenCreateReminderIcon = getIconOfSpecificScreen('createReminder')
    if screenCreateReminderIcon:
        screenCreateReminders.iconbitmap(screenCreateReminderIcon)
    screenCreateReminders.focus_set()
    screenCreateReminders.geometry("700x500")

    frameSportDay = tk.Frame(screenCreateReminders)
    labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
    labelSportDaySelected = tk.Label(
        frameSportDay,
        text="{}".format(datetime.datetime.now().strftime("%Y-%m-%d")) # Modify with date getted of db
    )
    labelSportDaySelected.grid(row=0, column=1)

    dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
    dadepickerButton['command'] = functools.partial(selectData, screenCreateReminders, labelSportDaySelected)
    dadepickerButton.grid(row=0, column=2)
    frameSportDay.pack(side=tk.TOP)

    sportOptions = [
        'esport 1',
        'esport 2',
        'esport 3',
        'esport'
    ]

    frameSportSelect = tk.Frame(screenCreateReminders)
    labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
    dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
    dropdownSport['values'] = sportOptions
    dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport))
    dropdownSport.grid(row=0, column=1)
    frameSportSelect.pack(side=tk.TOP)

    buttonSubmitReminder = ttk.Button(screenCreateReminders, text="Desar recordatori")
    buttonSubmitReminder['command'] = functools.partial(saveReminder)
    buttonSubmitReminder.pack()


    screenCreateReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateReminder, screenCreateReminders, buttonCreateReminder))

def buttonStatisticsListener(mainScreen, buttonStatistics):
    screenStatistics = tk.Toplevel(mainScreen)
    screenStatistics.winfo_toplevel().title("Sport log - ESTADÍSTIQUES")
    screenCreateReminderIcon = getIconOfSpecificScreen('statisticsScreen')
    if screenCreateReminderIcon:
        screenStatistics.iconbitmap(screenCreateReminderIcon)
    screenStatistics.focus_set()
    screenStatistics.geometry("700x500")
    buttonStatistics['state'] = 'disabled'
    #SpLog-CreateScreen ... do screen --> https://www.youtube.com/watch?v=8exB6Ly3nx0
    statistics()
    screenStatistics.protocol("WM_DELETE_WINDOW", functools.partial(onCloseStatistics, screenStatistics, buttonStatistics))

def buttonListRemindersListener(mainScreen, buttonListReminders):
    screenListReminders = tk.Toplevel(mainScreen)
    screenListReminders.winfo_toplevel().title("Sport log - LLISTAT RECORDATORIS")
    screenCreateReminderIcon = getIconOfSpecificScreen('remindersList')
    if screenCreateReminderIcon:
        screenListReminders.iconbitmap(screenCreateReminderIcon)
    screenListReminders.focus_set()
    screenListReminders.geometry("700x500")
    buttonListReminders['state'] = 'disabled'
    tk.Label(screenListReminders, text="Llistat recordatoris").pack(padx=10, pady=10)
    #SpLog-CreateScreen ... do list
    frameTree = tk.Frame(screenListReminders)
    tree = ttk.Treeview(frameTree)
    tree["columns"] = ("C1", "C2")
    tree.column("#0", width=70, minwidth=70, stretch=tk.NO)
    tree.column("C1", width=200, minwidth=200, stretch=tk.NO)
    tree.column("C2", width=200, minwidth=200, stretch=tk.NO)
    tree.heading("#0", text="ID", anchor=tk.W)
    tree.heading("C1", text="Esport", anchor=tk.W)
    tree.heading("C2", text="Dia esport", anchor=tk.W)

    for i in range(20):
        tree.insert("", i, text="Rem. {}".format(i), values=("esport","dia esport"))

    vsb = ttk.Scrollbar(frameTree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
        

    tree.pack(side="left", expand=True)
    vsb.pack(side='right', fill='y')
    frameTree.pack(padx=5, pady=5)
    screenListReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseListReminders, screenListReminders, buttonListReminders))
