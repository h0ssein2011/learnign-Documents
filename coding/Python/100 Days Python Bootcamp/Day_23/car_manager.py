from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(-180)
        self.x = random.randint(280,300)
        self.y = random.randint(-300,300)
        self.goto(self.x, self.y)
        self.move_speed = 0.1
        

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)
        