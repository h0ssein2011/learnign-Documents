from turtle import Turtle, Screen

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

for i in range(3,20):
    angle = -1 * int(360 / i)
    size = 100

    for i in range(i):
        new_turtle.forward(size)
        new_turtle.left(angle)
 



screen.exitonclick()

