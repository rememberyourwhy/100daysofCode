from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Ariel", 20, "italic"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Trivia API")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Scoreboard Label
        self.scoreboard_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scoreboard_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="HI",
            fill=THEME_COLOR,
            font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button Images
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        # Buttons
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.choice_true
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.choice_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        # Mainloop
        self.window.mainloop()

    def choice_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def choice_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the file")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
