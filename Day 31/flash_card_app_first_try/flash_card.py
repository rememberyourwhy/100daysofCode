from tkinter import *
from tkinter import messagebox
import json
from term import Term


# ----------------------------------- CONSTANTS --------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NOTE_FONT = "Ariel", 40, "italic"
WORD_NOTE_FONT = "Ariel", 60, "bold"
MAX_INDEX = 100
SMALLER_FONT = "Ariel", 40, "normal"


# --------------------------- CANVAS FLIP ---------------------------- #
def clicked(event):
    canvas.itemconfig(cv_img, image=card_back_img)
    canvas.itemconfig(cv_language_text, text="English")
    canvas.itemconfig(cv_word_text, text=term.value["English"])


# --------------------------- UPDATE THE CANVAS ---------------------- #
def update_the_canvas(index):
    global term
    term = Term(get_a_word(index))
    canvas.itemconfig(cv_img, image=card_front_img)
    canvas.itemconfig(cv_language_text, text="French")
    canvas.itemconfig(cv_word_text, text=term.value["French"])


# ----------------------------- UPDATE DATA TO WORDS.JSON ------------ #
def update_data():
    global term
    new_data = term.full_dict

    with open("words.json", mode="r") as data_file:
        data = json.load(data_file)
        data.update(new_data)
    with open("words.json", mode="w") as data_file:
        json.dump(data, data_file, indent=4)


# ------------------------------- I KNOW THIS WORD ------------------ #
def this_word_is_known():
    global term
    term.to_known()
    update_data()
    new_index = term.index + 1
    update_the_canvas(new_index)


# ------------------------------- I DON'T KNOW THIS WORD ------------------ #
def this_word_is_unknown():
    global term
    term.to_unknown()
    update_data()
    new_index = term.index + 1
    update_the_canvas(new_index)


# -------------------------------- REACHED MAX INDEX ------------------- #
def reached_max_index():
    canvas.unbind("<Button-1>")
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")
    canvas.itemconfig(cv_img, image=card_front_img)
    canvas.itemconfig(cv_language_text, text="REACHED THE END OF THIS DECK", font=SMALLER_FONT)
    canvas.itemconfig(cv_word_text, text="CLOSE THIS WINDOW", font=SMALLER_FONT)


# -------------------------------- GET NEXT WORD --------------------- #
def get_a_word(index):
    with open("words.json", mode="r") as data_file:
        data = json.load(data_file)
    try:
        is_known = data[str(index)]["known"]
    except KeyError:
        reached_max_index()
    else:
        if is_known:
            return get_a_word(index + 1)
        else:
            return {index: data[str(index)]}


# ----------------------------------- UI SETUP ---------------------- #


# ------- Window --------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Add Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# ------- Canvas --------- #
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

cv_img = canvas.create_image(400, 263, image=card_front_img)
cv_language_text = canvas.create_text(400, 150, text="French", font=LANGUAGE_NOTE_FONT)
try:
    term = Term(get_a_word(0))
except NameError:
    messagebox.showinfo(title="Congratulation", message="""
        This deck is already done, program will close after you close this box
    """)
    window.destroy()
else:
    cv_word_text = canvas.create_text(400, 263, text=term.value["French"], font=WORD_NOTE_FONT)
    canvas.grid(column=0, row=0, columnspan=2)
    canvas.bind("<Button-1>", clicked)

    # ------- Button ---------- #
    wrong_button = Button(image=wrong_img, command=this_word_is_unknown, highlightthickness=0)
    wrong_button.grid(column=0, row=1)
    right_button = Button(image=right_img, command=this_word_is_known, highlightthickness=0)
    right_button.grid(column=1, row=1)
    # Mainloop
    this_word_is_known()
    window.mainloop()
# First UI step
# I'll do the UI part
# First, make the canvas
# Then add front image to it
# Make two Label, one is "French", other one is the French word
# Add two buttons
# One is Wrong and one is right

# Grid setup
# two Label will take up two column, so their column span will be 2
# Get CSV inf
# make function get new word


# ALTERNATIVE SOLUTION:
# --------------------------------------------- IMPORT ALL TO UNKNOWN -------------------------------- #
# every new word imported from csv, we will update them to unknown word.
# each time we check a word. If they are known -> update them in known word
# else: just keep it stays there in unknown_word.json
# Cons: can not handle index iteration.

# ------------------------------------------ HAVING A GOOD DATA STRUCTURE ---------------------------- #
"""
    {ID :   {
                "French": "french_word",  # french_word is a string
                "English": "english_word",  # english_word is a string
                "known": None   # known value will first be initialized as None
                                # then it can be True or False
            }
    }
"""

# _______________________________ HOW TO ...? _________________________________________________________ #
# how to make canvas a button
# in other word, bind the canvas to the mouse:
# https://stackoverflow.com/questions/19369391/how-to-make-a-button-using-the-tkinter-canvas-widget
