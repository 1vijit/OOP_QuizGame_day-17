from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

var = 1
score = 0
total = 0
while var == 1:
    quiz=QuizBrain(question_bank)
    var=quiz.still_has_questions()
    response=quiz.next_question(total)
    score += response
    total += 1
    if total >11:
        var =0
    print(f"Your current score is {score}/{total}.")

print(f"Your final score was {score}/{total}.")




