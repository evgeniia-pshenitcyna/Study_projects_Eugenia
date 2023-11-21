from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    q_question = Question(text, answer)
    question_bank.append(q_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print("You've completed a quiz!")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}.")