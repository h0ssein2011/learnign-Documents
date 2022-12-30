from turtle import Turtle

class Score_board(Turtle):
    def __init__(self , x , y):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align='center' ,font=('Normal',50))


