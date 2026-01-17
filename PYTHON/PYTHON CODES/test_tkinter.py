import tkinter as tk
from tkinter import ttk
# 'data' is a tuple of choices
root = tk.Tk()
data = ("Option 1", "Option 2", "Option 3")
cb = ttk.Combobox(root, values=data, state='readonly')
cb.set("Option 1") # Set the default value
cb.grid(row=3, column=0, pady=5, padx=10, sticky='w')
root.title("My Grid App")
root.geometry("300x200")

# Define the action
def show():
    print("button clicked")

# Row 0: The Label
# sticky='w' keeps it left-aligned
lbl = tk.Label(root, text="This is a Label", fg='red', font=("Helvetica", 16))
lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='w')

# Row 1: The Button
btn = tk.Button(root, text="Click Me", fg='blue', command=show)
btn.grid(row=1, column=0, pady=5, padx=10, sticky='w')

# Row 2: The Entry (Password Field)
txtfld = tk.Entry(root, show="*", bd=5)
txtfld.grid(row=2, column=0, pady=5, padx=10, sticky='w')

root.mainloop()