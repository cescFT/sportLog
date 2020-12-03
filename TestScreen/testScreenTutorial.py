import tkinter as tk

def getText(event):
    print(event.widget.get())

def generateWindow():
    window = tk.Tk()
    greetings = tk.Label(text="Test test test label")
    greetings.pack()
    button = tk.Button(text="Click me")
    button.pack()
    inputUsr = tk.Entry(width=50)
    inputUsr.bind("<Return>", getText)
    inputUsr.pack()
    inputUsr.focus()
    window.mainloop()


if __name__ == "__main__":
    generateWindow()