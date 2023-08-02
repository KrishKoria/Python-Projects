class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}:{current_question.text} (True/False): ").lower()
        self.checking_answer(ans, current_question.answer)

    def checking_answer(self, given_ans, correct_answer):
        if given_ans == correct_answer.lower():
            print("Correct Answer!!")
            self.score += 1
        else:
            print("Wrong Answer")
        print(f"The correct Answer is {correct_answer}")
        print(f"Your Current Score is {self.score}/{self.question_number}")
        print("\n")
