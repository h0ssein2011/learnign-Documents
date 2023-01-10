from turtle import Turtle
MOVEMENT_SIZE = 10

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1
    
    def up(self):
        self.setheading(90)
        self.forward(MOVEMENT_SIZE)

    def down(self):
        self.setheading(270)
        self.forward(MOVEMENT_SIZE)
    
    def left(self):
        self.setheading(180)
        self.forward(MOVEMENT_SIZE)
    
    def right(self):
        self.setheading(0)
    
        
