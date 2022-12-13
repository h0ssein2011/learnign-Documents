from turtle import Turtle , Screen
import random


screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255)

y_positions =[-70,-40,-10,20,50,80,110]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


for i in range(len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-380 , y=y_positions[i])
    new_turtle.color(random_color())

screen.exitonclick()