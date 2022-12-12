from turtle import Turtle , Screen

new_turtle = Turtle()
screen = Screen()

def move_fd():
    new_turtle.forward(100)
def move_bw():
    new_turtle.backward(100)
def turn_left():
    new_turtle.left(90)
def turn_right():
    new_turtle.right(90)
def clear():
    new_turtle.clear()
    new_turtle.home()



screen.listen()
screen.onkey(fun = move_fd, key='w')
screen.onkey(fun = move_bw, key='s')
screen.onkey(fun = turn_left, key='a')
screen.onkey(fun = turn_right, key='d')
screen.onkey(fun = clear, key='c')





screen.exitonclick()