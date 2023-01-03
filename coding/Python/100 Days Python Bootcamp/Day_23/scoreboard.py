from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.score = 1
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
    
    def update_score_baord(self):
        self.score += 1