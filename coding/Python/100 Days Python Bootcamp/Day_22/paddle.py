from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()

        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(xcor,ycor)


    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)