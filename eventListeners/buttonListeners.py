import os
import sys
import tkinter as tk
import functools
from tkinter import ttk
from eventListeners.screenActions import *
from logsManager.sportLogManager import *
from logsManager.reminderManager import *
from logsManager.statisticsManager import *
from logsManager.dbConnection import execute
from tkcalendar import Calendar, DateEntry
import datetime

def getDuration(spinner, durationType, infoToSave):
    infoToSave[durationType] = spinner.get()

def getValueSelectedDifficulty(dropdownDifficulty, infoToSave):
    infoToSave['dificultat'] = dropdownDifficulty.get()

def getValueSelectedSport(dropdownSport, infoToSave):
    infoToSave['sport'] = dropdownSport.get()

def selectData(root, labelSportDaySelected, infoToSave):
    def print_sel():
        print(labelSportDaySelected)
        labelSportDaySelected['text'] = cal.selection_get()
        infoToSave['date'] = cal.selection_get()
        datepickerScreen.destroy()

    datepickerScreen = tk.Toplevel(root)
    datepickerScreen.winfo_toplevel().title("Sport log - SELECCIONA DATA")
    screenCalendarIcon = getIconOfSpecificScreen('selectData')
    if screenCalendarIcon:
        datepickerScreen.iconbitmap(screenCalendarIcon)
    datepickerScreen.wm_attributes("-topmost", 1)
    datepickerScreen.focus_force()
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

def buttonCreateLogListener(mainScreen, buttonCreateLog, treeView):
    infoToSave = {}
    screenFormCreateLog = tk.Toplevel(mainScreen)
    screenFormCreateLog.geometry("600x400")
    screenFormCreateLog.minsize(200, 200)
    screenIcon = getIconOfSpecificScreen('createLogScreen')
    if screenIcon:
        screenFormCreateLog.iconbitmap(screenIcon)
    screenFormCreateLog.winfo_toplevel().title("Sport log - CREAR LOG")
    screenFormCreateLog.wm_attributes("-topmost", 1)
    screenFormCreateLog.focus_force()
    buttonCreateLog["state"] = "disabled"
    #CREATING FORM TO NEW LOG
    
    # 1-Sport dropdown
    sportOptions = execute('SELECT nom_esport FROM esport')
    frameSportSelect = tk.Frame(screenFormCreateLog)
    labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
    dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
    dropdownSport['values'] = sportOptions
    dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport, infoToSave))
    dropdownSport.grid(row=0, column=1)
    frameSportSelect.pack(side=tk.TOP)

    # 2-SportDay
    frameSportDay = tk.Frame(screenFormCreateLog)
    labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
    labelSportDaySelected = tk.Label(
        frameSportDay,
        text="{}".format(datetime.datetime.now().strftime("%Y-%m-%d"))
    )
    infoToSave['date'] = datetime.datetime.strptime(labelSportDaySelected['text'], "%Y-%m-%d")
    labelSportDaySelected.grid(row=0, column=1)

    dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
    dadepickerButton['command'] = functools.partial(selectData, screenFormCreateLog, labelSportDaySelected, infoToSave)
    dadepickerButton.grid(row=0, column=2)

    frameSportDay.pack(side=tk.TOP)

    # 3- Duration
    frameDuration = tk.Frame(screenFormCreateLog)
    labelTimeElapsed = tk.Label(frameDuration, text = "Durada (h,m,s)").grid(row=0, column=0, padx=4, pady=10)
    hourPicker = ttk.Spinbox(frameDuration, from_=0, to=23, wrap=True, width=5, state="readonly")
    hourPicker['command'] = functools.partial(getDuration,hourPicker, 'hora', infoToSave)
    hourPicker.grid(row=0, column=1)
    tk.Label(frameDuration, text="h").grid(row=0,column=2)
    minutePicker = ttk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly")
    minutePicker['command'] = functools.partial(getDuration, minutePicker, 'minuts', infoToSave)
    minutePicker.grid(row=0, column=3)
    tk.Label(frameDuration, text="m").grid(row=0, column=4)
    secondsPicker = ttk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly")
    secondsPicker['command'] = functools.partial(getDuration, secondsPicker, 'segons', infoToSave)
    secondsPicker.grid(row=0, column=5)
    tk.Label(frameDuration, text="s").grid(row=0,column=6)

    frameDuration.pack(side=tk.TOP)
    
    # 4- Difficculty
    frameDifficulty = tk.Frame(screenFormCreateLog)
    labelDificulty = tk.Label(frameDifficulty ,text = "Dificultat").grid(row=0, column=0, padx=4, pady=10)

    difficultyOptions = execute ('SELECT dificultat FROM dificultat')
    dropdownDifficulty = ttk.Combobox(frameDifficulty, state="readonly")
    dropdownDifficulty['values'] = difficultyOptions
    dropdownDifficulty.bind('<<ComboboxSelected>>', lambda event: getValueSelectedDifficulty(dropdownDifficulty, infoToSave))
    dropdownDifficulty.grid(row=0, column=1)
    frameDifficulty.pack(side=tk.TOP)

    #Submit button new log
    frameButtonSubmitNewLog = tk.Frame(screenFormCreateLog)
    buttonSubmitNewLog = ttk.Button(frameButtonSubmitNewLog, text="Desar nou log")
    buttonSubmitNewLog['command'] = functools.partial(saveNewSportLog, infoToSave, screenFormCreateLog, buttonCreateLog, treeView)
    buttonSubmitNewLog.pack(padx=50, pady=50)
    frameButtonSubmitNewLog.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    

    screenFormCreateLog.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateLogForm, screenFormCreateLog, buttonCreateLog))

def buttonEditLogListener(mainScreen, buttonEditLog, treeView):
    if treeView.selection():
        screenEditLog = tk.Toplevel(mainScreen)
        screenEditLog.geometry("600x400")
        screenEditLogIcon = getIconOfSpecificScreen('editLogScreen')
        if screenEditLogIcon:
            screenEditLog.iconbitmap(screenEditLogIcon)
        screenEditLog.winfo_toplevel().title("Sport log - EDITAR LOG(s) SELECCIONATS")
        screenEditLog.wm_attributes("-topmost", 1)
        screenEditLog.focus_force()
        buttonEditLog['state'] = 'disabled'

        sportOptions = execute("SELECT nom_esport FROM esport")

        difficultyOptions = execute("SELECT dificultat FROM dificultat")

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
            infoToSave = {}
            infoToSave['id'] = treeView.item(i)['text'].split(" ")[1]
            infoToSave['dificultat'] = treeView.item(i)['values'][3]
            infoToSave['sport'] = treeView.item(i)['values'][0]
            infoToSave['date'] = datetime.datetime.strptime(treeView.item(i)['values'][2], '%d-%m-%Y')
            infoToSave['hora'] = treeView.item(i)['values'][1].split(":")[0].split(" ")[0]
            infoToSave['minuts'] = treeView.item(i)['values'][1].split(":")[1].split(" ")[0]
            infoToSave['segons'] = treeView.item(i)['values'][1].split(":")[2].split(" ")[0]
            frameFormEditLogForm = tk.Frame(frameFormEditLog, borderwidth=2, relief="groove")
            # 1-Sport dropdown
            frameSportSelect = tk.Frame(frameFormEditLogForm)
            labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
            dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
            dropdownSport['values'] = sportOptions
            index = 0
            for sp in sportOptions:
                if sp[0] == treeView.item(i)['values'][0]:
                    break
                index = index + 1
            dropdownSport.current(index)
            dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport, infoToSave))
            dropdownSport.grid(row=0, column=1)
            frameSportSelect.pack(side=tk.TOP)
            
            # 2-SportDay
            frameSportDay = tk.Frame(frameFormEditLogForm)
            labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
            labelSportDaySelected = tk.Label(
                frameSportDay,
                text="{}".format(treeView.item(i)['values'][2])
            )
            labelSportDaySelected.grid(row=0, column=1)

            dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
            dadepickerButton['command'] = functools.partial(selectData, screenEditLog, labelSportDaySelected, infoToSave)
            dadepickerButton.grid(row=0, column=2)
            frameSportDay.pack(side=tk.TOP)

            # 3- Duration
            frameDuration = tk.Frame(frameFormEditLogForm)
            labelTimeElapsed = tk.Label(frameDuration, text = "Durada (h,m,s)").grid(row=0, column=0, padx=4, pady=10)
            hourPicker = tk.Spinbox(frameDuration, from_=1, to=23, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=int(treeView.item(i)['values'][1].split(":")[0].split(" ")[0])))
            hourPicker['command'] = functools.partial(getDuration,hourPicker, 'hora', infoToSave)
            hourPicker.grid(row=0, column=1)
            tk.Label(frameDuration, text="h").grid(row=0,column=2)
            minutePicker = tk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=int(treeView.item(i)['values'][1].split(":")[1].split(" ")[0])))
            minutePicker['command'] = functools.partial(getDuration,minutePicker, 'minuts', infoToSave)
            minutePicker.grid(row=0, column=3)
            tk.Label(frameDuration, text="m").grid(row=0, column=4)
            secondsPicker = tk.Spinbox(frameDuration, from_=0, to=59, wrap=True, width=5, state="readonly", textvariable=tk.IntVar(value=int(treeView.item(i)['values'][1].split(":")[2].split(" ")[0])))
            secondsPicker['command'] = functools.partial(getDuration,secondsPicker, 'segons', infoToSave)
            secondsPicker.grid(row=0, column=5)
            tk.Label(frameDuration, text="s").grid(row=0,column=6)

            frameDuration.pack(side=tk.TOP)
            
            # 4- Difficculty
            frameDifficulty = tk.Frame(frameFormEditLogForm)
            labelDificulty = tk.Label(frameDifficulty ,text = "Dificultat").grid(row=0, column=0, padx=4, pady=10)

            dropdownDifficulty = ttk.Combobox(frameDifficulty, state="readonly")
            dropdownDifficulty['values'] = difficultyOptions
            dropdownDifficulty.bind('<<ComboboxSelected>>', lambda event: getValueSelectedDifficulty(dropdownDifficulty, infoToSave))
            index = 0
            for difficulty in difficultyOptions:
                if difficulty[0] == treeView.item(i)['values'][3]:
                    break
                index = index + 1
            dropdownDifficulty.current(index)
            dropdownDifficulty.grid(row=0, column=1)
            frameDifficulty.pack(side=tk.TOP)

            #Submit button edit log
            frameButtonSubmitEditLog = tk.Frame(frameFormEditLogForm)
            buttonSubmitNewLog = ttk.Button(frameButtonSubmitEditLog, text="Editar log")
            buttonSubmitNewLog['command'] = functools.partial(editSportLog, infoToSave, treeView, screenEditLog)
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
                deleteSportLog(infoToDeleteFromDB)
                treeView.delete(item)
    else:
        tk.messagebox.showwarning(title="Eliminar log(s)", message="Selecciona almenys un dels logs mostrat en el llistat per a eliminar-lo")

def buttonCreateReminderListener(mainScreen, buttonCreateReminder):
    infoToSave = {}
    infoToSave['date'] = datetime.datetime.now().date()
    screenCreateReminders = tk.Toplevel(mainScreen)
    buttonCreateReminder['state'] = 'disabled'
    screenCreateReminders.winfo_toplevel().title("Sport log - CREAR RECORDATORI")
    screenCreateReminderIcon = getIconOfSpecificScreen('createReminder')
    if screenCreateReminderIcon:
        screenCreateReminders.iconbitmap(screenCreateReminderIcon)
    screenCreateReminders.wm_attributes("-topmost", 1)
    screenCreateReminders.focus_force()
    screenCreateReminders.geometry("700x500")

    frameSportDay = tk.Frame(screenCreateReminders)
    labelSportDay = tk.Label(frameSportDay ,text = "Dia esport").grid(row=0, column=0, padx=4, pady=10)
    labelSportDaySelected = tk.Label(
        frameSportDay,
        text="{}".format(datetime.datetime.now().strftime("%Y-%m-%d"))
    )
    labelSportDaySelected.grid(row=0, column=1)

    dadepickerButton = ttk.Button(frameSportDay, text='Modificar data')
    dadepickerButton['command'] = functools.partial(selectData, screenCreateReminders, labelSportDaySelected, infoToSave)
    dadepickerButton.grid(row=0, column=2)
    frameSportDay.pack(side=tk.TOP)

    sportOptions = execute("SELECT nom_esport FROM esport")

    frameSportSelect = tk.Frame(screenCreateReminders)
    labelSportSelect = tk.Label(frameSportSelect ,text = "Selecciona esport").grid(row=0, column=0, padx=4, pady=10)
    dropdownSport = ttk.Combobox(frameSportSelect, state="readonly")
    dropdownSport['values'] = sportOptions
    dropdownSport.bind('<<ComboboxSelected>>', lambda event: getValueSelectedSport(dropdownSport, infoToSave))
    dropdownSport.grid(row=0, column=1)
    frameSportSelect.pack(side=tk.TOP)

    frameHour = tk.Frame(screenCreateReminders)
    labelHour = tk.Label(frameHour, text="Escriu la hora (hh:mm)").grid(row=0, column=0, padx=4, pady=10)
    textboxHour = ttk.Entry(frameHour)
    
    buttonSubmitReminder = ttk.Button(frameHour, text="Desar recordatori")
    buttonSubmitReminder['command'] = functools.partial(saveReminder, infoToSave, buttonCreateReminder, screenCreateReminders, textboxHour)
    buttonSubmitReminder.grid(row=1, column=0, padx=4, pady=10)
    textboxHour.grid(row=0, column=1)
    frameHour.pack(side=tk.TOP)

    screenCreateReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseCreateReminder, screenCreateReminders, buttonCreateReminder))

def buttonStatisticsListener(mainScreen, buttonStatistics):
    buttonStatistics['state'] = 'disabled'
    screenStatisticsIcon = getIconOfSpecificScreen('statisticsScreen')
    statistics(screenStatisticsIcon, buttonStatistics)

def buttonListRemindersListener(mainScreen, buttonListReminders):
    screenListReminders = tk.Toplevel(mainScreen)
    screenListReminders.winfo_toplevel().title("Sport log - LLISTAT RECORDATORIS")
    screenCreateReminderIcon = getIconOfSpecificScreen('remindersList')
    if screenCreateReminderIcon:
        screenListReminders.iconbitmap(screenCreateReminderIcon)
    screenListReminders.wm_attributes("-topmost", 1)
    screenListReminders.focus_force()
    screenListReminders.geometry("700x500")
    buttonListReminders['state'] = 'disabled'
    tk.Label(screenListReminders, text="Llistat recordatoris").pack(padx=10, pady=10)

    frameTree = tk.Frame(screenListReminders)
    tree = ttk.Treeview(frameTree)
    tree["columns"] = ("C1", "C2")
    tree.column("#0", width=70, minwidth=70, stretch=tk.NO)
    tree.column("C1", width=200, minwidth=200, stretch=tk.NO)
    tree.column("C2", width=200, minwidth=200, stretch=tk.NO)
    tree.heading("#0", text="ID", anchor=tk.W)
    tree.heading("C1", text="Esport", anchor=tk.W)
    tree.heading("C2", text="Dia esport", anchor=tk.W)

    reminders = execute("SELECT r.id, e.nom_esport, r.dia FROM recordatori r INNER JOIN esport e ON r.esport = e.id ORDER BY r.dia DESC")
    
    for reminder in reminders:
        tree.insert("", reminder[0], text="Rem. {}".format(reminder[0]), values=(reminder[1],reminder[2].strftime("%d-%m-%Y")))

    vsb = ttk.Scrollbar(frameTree, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
        

    tree.pack(side="left", expand=True)
    vsb.pack(side='right', fill='y')
    frameTree.pack(padx=5, pady=5)
    screenListReminders.protocol("WM_DELETE_WINDOW", functools.partial(onCloseListReminders, screenListReminders, buttonListReminders))
