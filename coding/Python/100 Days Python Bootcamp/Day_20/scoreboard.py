from turtle import Turtle
""" create a class to inherit from turtle and shows scroe above the screen and clauclate the score """
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'score : {self.score}', move=False,align='center',font=('Arial',24,'normal'))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()