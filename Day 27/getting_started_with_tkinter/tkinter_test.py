# from tkinter import *
#
# FONT = "Arial", 24, "bold"
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# # Creating Label
#
# my_label = Label(text="I am a Label", font=FONT)
# my_label.pack()
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
# # Button
#
#
# def button_clicked():
#     inf = user_input.get()
#     my_label.config(text=inf)
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
# # Entry
# user_input = Entry(width=10)
# user_input.pack()
#
# window.mainloop()

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()
# So label class has a method called config
# But text class doesn't have the same function
# Instead, in oder to edit content in text object
# We can .insert() and delete.text()
# Which mean we can delete all and insert to do the same thing with label.config


# Buttons
def action():
    pass
    # content = text.get("1.0", END).strip()
    # content = f"{content} dang yeu"
    # print(content)
    # text.delete("1.0", END)
    # # text.insert("1.0", ")
    # text.insert(INSERT, content)
    # print("ACT DONE")


# calls action() when pressed
button = Button(text="Reveal su that", command=action)
button.pack()

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Ai dang yeu?")
# Gets text in entry
# print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
# cursor here is text cursor not the mouse
text.focus()
# Adds some text to begin with.
text.insert(INSERT, "")
# Get current value in textbox at line 1, character 0
# print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    pass


spinbox = Spinbox(from_=0, to=12, width=5, command=spinbox_used, text="Month")
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print("checked" if checked_state.get() else "unchecked")


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()