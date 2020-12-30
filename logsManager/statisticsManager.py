
import tkinter
import numpy as np
import functools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from eventListeners.screenActions import onCloseStatistics

# llegir logs i estudiarlos

def statistics(screenStatisticsIcon, buttonStatistics):
    screenStatistics = tkinter.Tk()
    screenStatistics.wm_title("Sport log - ESTADÍSTIQUES")
    if screenStatisticsIcon:
        screenStatistics.iconbitmap(screenStatisticsIcon)
    screenStatistics.wm_attributes("-topmost", 1)
    screenStatistics.focus_force()
    screenStatistics.geometry("700x500")

    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    canvas = FigureCanvasTkAgg(fig, master=screenStatistics)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, screenStatistics)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    def _quit():
        buttonStatistics['state'] = 'normal'
        screenStatistics.quit()
        screenStatistics.destroy()


    button = tkinter.Button(master=screenStatistics, text="Tancar", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    screenStatistics.protocol("WM_DELETE_WINDOW", functools.partial(onCloseStatistics, screenStatistics, buttonStatistics))
    tkinter.mainloop()