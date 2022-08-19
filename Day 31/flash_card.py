from tkinter import *


# ----------------------------------- CONSTANTS --------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_NOTE_FONT = "Ariel", 40, "italic"
WORD_NOTE_FONT = "Ariel", 60, "bold"


# ------------------------------- I KNOW THIS WORLD ------------------ #
def this_word_is_known():
    pass


# ------------------------------- I DON'T KNOW THIS WORLD ------------------ #
def this_word_is_unknown():
    pass


# -------------------------------- GET NEXT WORD --------------------- #
def get_a_word():
    return "word"


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
new_word = get_a_word()
cv_word_text = canvas.create_text(400, 263, text=new_word, font=WORD_NOTE_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# ------- Button ---------- #
wrong_button = Button(image=wrong_img, command=this_word_is_unknown, highlightthickness=0)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_img, command=this_word_is_known, highlightthickness=0)
right_button.grid(column=1, row=1)
# Mainloop

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

