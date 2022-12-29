# import colorgram as cg 
from turtle import Turtle , Screen
import random

colors = [ (202, 166, 109), (240, 246, 241), (152, 73, 47), 
    (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184),
    (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156),
    (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), 
    (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]


new_turtle = Turtle()
screen = Screen()
# screen.bgcolor()
screen.colormode(255)
new_turtle.penup()
new_turtle.speed('fastest')
new_turtle.hideturtle()

new_turtle.penup()
new_turtle.setposition(-300,-300)
for i in range(1,13):
    for j in range(13):
        new_turtle.dot(20,random.choice(colors))
        new_turtle.forward(50)
    new_turtle.setposition(-300 , -300 + 75 * i)






screen.exitonclick()    