import tkinter as tk
from tkinter import ttk

headings = ["Heading0", "Heading1", "Heading2", "Heading3"]

root = tk.Tk()
root.title("Add headings")

frame1 = tk.Frame(root)
frame1.pack()

tree = ttk.Treeview(frame1)
tree["columns"] = ("C1", "C2")
tree.column("#0", width=500, minwidth=400, stretch=tk.NO)
tree.column("C1", width=200, minwidth=200, stretch=tk.NO)
tree.column("C2", width=200, minwidth=200, stretch=tk.NO)
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("C1", text="Type", anchor=tk.W)
tree.heading("C2", text="Index", anchor=tk.W)

t = {}

for i in range(5):
    t[i] = tree.insert("", i, text="Example " + str(i), values=("val1", "val2"))
tree.pack(expand=True, fill="both")



tree2 = ttk.Treeview(frame1)


tree2.pack(expand=True, fill="both")

root.mainloop()