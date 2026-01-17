import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Combobox Example")
# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["Option 1", "Option 2","Option 3"], state='readonly')
combo_box.pack(pady=5)
# Set default value
combo_box.set("Option 1")
root.mainloop()