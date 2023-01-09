from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):

        self.car_list = []
        

    def move_car(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)
    
    def create_car(self):
        rand_number = random.randint(1,6)
        if rand_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(-180)
            y = random.randint(-280,280)
            new_car.goto(300, y)
            self.car_list.append(new_car)
        
        