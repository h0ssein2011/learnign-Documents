from turtle import Turtle

class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100,180)
        self.write(self.r_score , align='center',font=('Tahoma', 50, 'normal'))

        self.goto(-100,180)
        self.write(self.l_score , align='center',font=('Tahoma', 50, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def l_point(self):
        self.l_score += 1
        self.update_score()