from tkinter import *


THEME_COLOR = "#375362"
FONT = "Ariel", 20, "italic"


class QuizInterface:

    def __init__(self):
        # Window
        self.window = Tk()
        self.window.title("Trivia API")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Scoreboard Label
        self.scoreboard_label = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.scoreboard_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="HI",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Buttons
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.choice_true
        )
        self.true_button.grid(row=2, column=0)
        # self.false_button = Button(image=false_image, highlightthickness=0, command=self.choice_false)
        # self.true_button.grid(row=2, column=1)

        self.window.mainloop()

    def choice_true(self):
        pass

    def choice_false(self):
        pass
