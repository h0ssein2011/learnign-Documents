from turtle import Turtle ,Screen

my_turtle = Turtle()
screen = Screen()
screen.bgcolor('orange')


def turtle_dashing(turtle,length = 10,steps = 10):
    for i in range(length):
        turtle.forward(steps)
        turtle.penup()
        turtle.forward(steps)
        turtle.pendown()

turtle_dashing(my_turtle)
screen.exitonclick()