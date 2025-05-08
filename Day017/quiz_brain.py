class QuizBrain:

    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self,user_ans,crt_answer):
        if user_ans.lower() == crt_answer.lower():
            self.score += 1
            print("You got it Right!")
        else:
            print(f"That's Wrong, its {crt_answer}")
        print(f"Your current score: {self.score}/{self.q_number}")
        print("\n")

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
