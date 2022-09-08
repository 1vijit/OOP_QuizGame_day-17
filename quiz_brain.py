class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self, total):
        current_ques = self.question_list[total]
        response = input(f"Q.{self.question_number}: {current_ques.text} (True/False)?: ")
        response = response.capitalize()
        self.question_number += 1
        print(self.question_number)
        print(f"The correct answer was {current_ques.answer}")
        if response == current_ques.answer:
            print(f"You got it right")
            return 1
        else:
            print(f"You got it wrong")
            return 0

    def still_has_questions(self):
        length = len(self.question_list)
        if length > self.question_number:
            return 1
        else:
            return 0

