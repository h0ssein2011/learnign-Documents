from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x = 350):
        super().__init__()
        self.x = x
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.hideturtle()
        self.penup()
        self.goto( self.x, 0)
        self.showturtle()
       
    
    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)    
        
    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
        
