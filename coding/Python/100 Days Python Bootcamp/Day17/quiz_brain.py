class Quiz_Brain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_bank) 


    
    def next_question(self):
        current_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number} :{current_question.text}")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('That was right')
            self.score += 1
        else:
            print('That was not right answer the right answer was: ')
        print('correct answer is :',correct_answer)
        print(f'Your score is {self.score} / {self.question_number}')

   
    

        
