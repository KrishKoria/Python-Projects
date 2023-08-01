from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(text=question_text, answer=question_answer)
    question_bank.append(new_q)

# for q in question_bank:
#     print(q.text)
#     print(q.answer)

quiz = QuizBrain(question_bank)
quiz.next_question()
