import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")

        self.color("blue")
        self.penup()
        self.refresh()
    
    def refresh(self):
        random_x_loc = random.randint(-280,280)
        random_y_loc = random.randint(-280,280)
        self.goto(random_x_loc,random_y_loc)
 
          