class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:{question.text} (True/False): ")
