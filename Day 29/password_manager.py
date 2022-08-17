from tkinter import *
from password_generator import random_easy, random_hard
# ---------------------------- CONSTANTS ---------------------#
WIDTH_C1 = 35
FONTNAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_easy = random_easy(4, 4, 4)
    password_hard = random_hard(password_easy)
    result = ''.join(password_hard)
    password_entry.delete(0, "end")
    password_entry.insert(0, result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def check_missing_fields():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    if website and email_username and password:
        save_password()
    else:
        error_popup = Toplevel(window, padx=20, pady=20)
        error_popup.geometry("325x100")
        error_popup.title("Missing Fields")
        error_label = Label(error_popup, text="Your form is missing a field or more, check again")
        error_label.grid(column=0, row=0)


def save_password():
    # get
    email_username = email_username_entry.get()
    password = password_entry.get()
    # create popup window
    popup = Toplevel(window, padx=20, pady=20)
    popup.geometry("325x125")
    popup.title("Final Check")
    # last check label and decision buttons
    last_check_label = Label(popup, text="Are you sure you want to save this account to data?")
    last_check_label.grid(row=0, column=0, columnspan=2, sticky="ew")
    show_info_1 = Label(popup, text=email_username)
    show_info_1.grid(row=1, column=0, columnspan=2, sticky="ew")
    show_info_2 = Label(popup, text=password)
    show_info_2.grid(row=2, column=0, columnspan=2, sticky="ew")

    def no_button():
        popup.destroy()
    button_no = Button(popup, text="No", command=no_button, width=10)
    button_no.grid(row=3, column=1)
    # write to file

    def yes_button():
        with open(file="data.txt", mode="a") as data:
            data.write(f"{email_username}\n{password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    button_yes = Button(popup, text="Yes", command=yes_button, width=10)
    button_yes.grid(row=3, column=0)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=280, height=280)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(140, 140, image=my_pass_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=WIDTH_C1)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
email_username_entry = Entry(width=WIDTH_C1)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Button
generate_password_button = Button(text="Generate Password", command=generate_password, width=16)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", command=check_missing_fields, width=WIDTH_C1)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


def main():
    window.mainloop()


main()
