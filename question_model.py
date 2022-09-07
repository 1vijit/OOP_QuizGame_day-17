class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


user1 = Question("2+3=5","True")
print(user1.text)
