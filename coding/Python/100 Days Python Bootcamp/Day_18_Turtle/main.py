from turtle import Turtle, Screen
from random import choice
new_turtle = Turtle()
screen = Screen()
screen.bgcolor("orange")

new_turtle.shape('turtle')

# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)

colors = """ White
Yellow
Blue
Red
Green
Black
Brown
Azure
Ivory
Teal
Silver
Purple
blue
green
Gray
Orange
Maroon
Charcoal
Aquamarine
Coral"""
colors = [c for c in colors.split()]

for i in range(3,20):
    angle = -1 * int(360 / i)
    size = 100
    new_turtle.pencolor(choice(colors))

    for i in range(i):
        new_turtle.forward(size)
        new_turtle.left(angle)
        
        

 
screen.exitonclick()

