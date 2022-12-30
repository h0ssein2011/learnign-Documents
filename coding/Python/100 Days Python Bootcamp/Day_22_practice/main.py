from turtle import Screen 
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_r = Paddle(x = 350)
paddle_l = Paddle(x = -350)

screen.listen()
screen.onkey(paddle_r.up ,'Up')
screen.onkey(paddle_r.down ,'Down')
screen.onkey(paddle_l.up ,'w')
screen.onkey(paddle_l.down ,'s')

ball = Ball()
score_r = Score_board(80,200)
score_l = Score_board(-80,200)




games_on = True
while games_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision detection with top and bottom
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # collision detection with paddle
    if (ball.xcor() > 320 and ball.distance(paddle_r) < 50) or (ball.xcor() < -320 and ball.distance(paddle_l) < 50):
        ball.bounce_x()

        

    #ditect collision with right 
    if ball.xcor() > 390 and ball.distance(paddle_r) > 15:
        ball.reset_location()
        score_l.score += 1 
        score_l.update_scoreboard()


    #ditect collision with left 
    if ball.xcor() < -390 and ball.distance(paddle_r) > 15:
        ball.reset_location()
        score_r.score += 1 
        score_r.update_scoreboard()


















screen.exitonclick()