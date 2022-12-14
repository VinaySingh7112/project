from ast import While
from matplotlib.pyplot import text
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank[4].answer)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have a completed the quiz ")
print(f"You final score was: {quiz.score}/{quiz.question_number} ")