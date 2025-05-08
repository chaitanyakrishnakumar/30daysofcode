from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = Question(item["text"],item["answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz🤗")
print(f"Your final score was: {quiz.score}/{quiz.q_number}")
