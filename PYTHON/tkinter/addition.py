import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 + num2 
        label_result.config(text=f"Result: {result}")  # Fixed: Changed 'Label_result' to 'label_result' to match the variable name
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Addition Using Tkinter")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter Number 1:")
label1.place(x=30, y=30)

entry1 = tk.Entry(root)
entry1.place(x=140, y=30)

label2 = tk.Label(root, text="Enter Number 2:")
label2.place(x=30, y=60)

entry2 = tk.Entry(root)
entry2.place(x=140, y=60)

btn = tk.Button(root, text="Add", command=add_numbers)
btn.place(x=70, y=90)

label_result = tk.Label(root, text="Result: ")
label_result.place(x=70, y=130)

root.mainloop()