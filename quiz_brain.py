class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_ques = self.question_list[self.question_number]
        response = input(f"Q.{self.question_number+1}: {current_ques.text} (True/False)?: ")
        response = response.lower()
        self.question_number += 1
        return response

    def still_has_questions(self):
        length = len(self.question_list)
        if length > self.question_number:
            return 1
        else:
            return 0

