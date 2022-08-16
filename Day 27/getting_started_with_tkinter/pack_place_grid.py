from tkinter import *


MILES_KMS_MULTI = 1.609344
FONT = "Arial", 12, "normal"


window = Tk()
window.title("Miles to Kms converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=1)
kms_label = Label(text="Kms", font=FONT)
kms_label.grid(column=3, row=2)
result_label = Label(text="0", font=FONT)
result_label.grid(column=2, row=2)
bridge_label = Label(text="is equal to", font=FONT)
bridge_label.grid(column=1, row=2)


def button_clicked():
    val_miles = int(input_entry.get())
    val_kms = val_miles * MILES_KMS_MULTI
    val_kms = int(val_miles)
    result_label.config(text=str(val_kms))


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

# Entry
input_entry = Entry(width=10)
input_entry.grid(column=2, row=1)
input_entry.focus()

mainloop()
# grid uses relative position, good to use
