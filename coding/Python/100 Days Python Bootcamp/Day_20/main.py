from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.title('My snake Game')
screen.tracer(0)

Turtles =[]
for i in range(3):
    new_turtle = Turtle('square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.setposition(i*-10,0)
    Turtles.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    for turtle in Turtles:
        turtle.forward(10)

    
    game_is_on = False


screen.exitonclick()