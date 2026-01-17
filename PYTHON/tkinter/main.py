from tkinter import *

# Create the main window
window = Tk()
window.title('MY APP')
window.geometry("1000x1256+10+20")  # Set window size and position ("widthxheight+XPOS+YPOS")

# Create variables for Checkbuttons
var1 = IntVar()
# Checkbutton for male selection
Checkbutton(window, text='male', variable=var1).grid(row=0, sticky=W)

var2 = IntVar()
# Checkbutton for female selection
Checkbutton(window, text='female', variable=var2).grid(row=1, sticky=W)

# Create variable for Radiobuttons
v = IntVar()
# Radiobutton for Python selection
Radiobutton(window, text='Python', variable=v, value=1).grid(row=2, sticky=W)
# Radiobutton for Programming selection
Radiobutton(window, text='Programming', variable=v, value=2).grid(row=3, sticky=W)

# Label widget displaying initial text
lbl = Label(window, text="This is my initial app", fg='black', font=("Times new roman", 24))
lbl.place(relx=0.5, rely=0.5, anchor='center')

# Button widget
btn = Button(window, text="My Button", fg="blue")
btn.place(x=80, y=100)

# Entry widget with default text
entry_var = StringVar(value="This is Entry Widget")  # Variable to hold entry text
txtfld = Entry(window, textvariable=entry_var, bg='black', fg='white', bd=5)
txtfld.place(x=80, y=130)

# Educational content about Tkinter widgets
# Label explaining Checkbutton
edu_check = Label(window, text="Checkbutton: A widget that allows users to select multiple options. Each has its own variable.", fg='blue', font=("Arial", 12))
edu_check.place(x=80, y=160)

# Label explaining Radiobutton
edu_radio = Label(window, text="Radiobutton: A widget for selecting one option from a group. All share the same variable.", fg='blue', font=("Arial", 12))
edu_radio.place(x=80, y=180)

# Label explaining Label
edu_label = Label(window, text="Label: A widget used to display text or images. It doesn't interact with the user.", fg='blue', font=("Arial", 12))
edu_label.place(x=80, y=200)

# Label explaining Button
edu_button = Label(window, text="Button: A widget that performs an action when clicked. Can be bound to a function.", fg='blue', font=("Arial", 12))
edu_button.place(x=80, y=220)

# Label explaining Entry
edu_entry = Label(window, text="Entry: A single-line text input field. Users can type text here.", fg='blue', font=("Arial", 12))
edu_entry.place(x=80, y=240)

# Start the main event loop
window.mainloop()