from turtle import Turtle , Screen
import random

smg = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor('orange')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


smg.speed('fastest')
left_step = 5
for i in range(int(360/left_step)):
    smg.color(random_color())
    smg.circle(radius=100)
    smg.left(left_step)



screen.exitonclick()