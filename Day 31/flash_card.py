from tkinter import *
import json


# ----------------------------------- CONSTANTS --------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NOTE_FONT = "Ariel", 40, "italic"
WORD_NOTE_FONT = "Ariel", 60, "bold"


# ------------------------------- I KNOW THIS WORLD ------------------ #
def this_word_is_known():
    """
    # save this known word to known_word json
    # UPDATE THE CANVAS
    """
    known_word_french = new_word["French"]
    known_word_english = new_word["English"]
    new_data = {index :{"French" :known_word_french,
                        "English":known_word_english,
                        "known": False
                        }
                }

    """
    # Syntax of this function:
    # var_to_be_assigned = 
    # canvas.itemcget(item_id, datatype)
    # item_id (the one that canvas.create_text or canvas.create_image return)
    # datatype : "text" or "image"
    """
    with open("known_word.json", mode="w") as known_word_file:
        json.dump(new_data, known_word_file, indent=4)
    update_the_canvas()


# ------------------------------- I DON'T KNOW THIS WORLD ------------------ #
def this_word_is_unknown():
    """
    # save this unknown word to unknown_word json
    # UPDATE THE CANVAS
    """
    unknown_word_french = new_word["French"]
    unknown_word_english = new_word["English"]
    ew_data = {index: {"French": known_word_french,
                       "English": known_word_english,
                       "known": False
                       }
               }
    with open("unknown_word.json", mode="w") as unknown_word_file:
        json.dump(new_data, unknown_word_file, indent=4)
    update_the_canvas()


# -------------------------------- GET NEXT WORD --------------------- #
def get_a_word(index):
    with open("words.json", mode="r") as words_file:
        data = json.load(words_file)
    word =


# --------------------------- UPDATE THE CANVAS ---------------------- #
def update_the_canvas():

    # Call get_next_word function
    # the return value will be 1: that word in French, 2: that word in English
    # updating the canvas: with English face
    pass

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

cv_front_img = canvas.create_image(400, 263, image=card_front_img)
cv_language_text = canvas.create_text(400, 150, text="French", font=LANGUAGE_NOTE_FONT)
index, new_word = [get_a_word()]
cv_word_text = canvas.create_text(400, 263, text=new_word[0], font=WORD_NOTE_FONT)
canvas.grid(column=0, row=0, columnspan=2)

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