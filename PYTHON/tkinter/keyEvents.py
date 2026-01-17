import tkinter as tk
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
root = tk.Tk()
root.title("Advanced Event Handling Example")
root.bind("<KeyPress>", on_key_press)
root.mainloop()