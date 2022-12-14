from turtle import Turtle , Screen
import random


screen = Screen()
screen.setup(width=1000, height=800)
screen.colormode(255)

y_positions =[-70,-40,-10,20,50,80,110]

colors =['yellow', 'green', 'orange', 'black','red','blue','purple']
bet_turtle = screen.textinput('User data',f'Which colors do you think will win? {colors}')


Turtles = []
for i in range(len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-450 , y=y_positions[i])
    new_turtle.color(colors[i])
    Turtles.append(new_turtle)

win_pos_x = 400
games_running = True

while games_running:
    idx = 0
    for turtle in Turtles:
        mv_amount = random.randint(1,10)
        turtle.forward(mv_amount)
        if turtle.pos()[0] >= win_pos_x:
            games_running = False
            # print(colors[idx],'wins')
            win_color = colors[idx]
        
        
        idx += 1
if bet_turtle == win_color:
    print('Great you predict it correctly')

else :
    print(f'Sorry you said {bet_turtle} will win but {win_color} won')
            
screen.exitonclick()