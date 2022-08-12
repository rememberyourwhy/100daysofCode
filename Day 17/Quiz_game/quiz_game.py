from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# This OOP is independent so that if we change here and there in the database
# We don't have to change any line of code in the other modules
# For example, if question_data change it data structure, or its dictionary key name
# We can simply change the code here in snake_game_day_24.py to fix it.
# We don't have to change code that is in quiz_brain.py
