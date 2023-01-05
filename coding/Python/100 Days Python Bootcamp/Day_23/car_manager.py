from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        

    def move_car(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def create_car(self):
        rand_number = random.randint(1,6)
        if rand_number == 1:
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=3)
            self.color(random.choice(COLORS))
            self.penup()
            self.setheading(-180)
            self.y = random.randint(-280,280)
            self.goto(300, self.y)
            self.car_list.append(self)
            print(self.car_list)
        
        