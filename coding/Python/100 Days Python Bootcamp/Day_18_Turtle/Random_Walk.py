from turtle import Turtle , Screen
import random

my_turtle = Turtle()
screen = Screen()
screen.bgcolor('orange')
screen.bgcolor('orange')

colors = """ White
Yellow
Blue
Red
Green
Black
Brown
Azure
Ivory
Silver
Purple
blue
green
Gray
Orange
Maroon
Aquamarine
"""
colors = [c.lower() for c in colors.split()]

angles =[45,90,135,180,270]
my_turtle.pensize(15)

my_turtle.speed('fastest')
for i in range(500):
    my_turtle.pencolor(random.choice(colors))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(angles))   
    

screen.exitonclick()

