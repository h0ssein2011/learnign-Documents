from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_Board
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

score_board = Score_Board()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up ,'Up')
screen.onkey(r_paddle.go_down ,'Down')
screen.onkey(l_paddle.go_up ,'w')
screen.onkey(l_paddle.go_down ,'s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collisions with top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    
    # detect collosion with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

    

        
    

  


  

        


screen.exitonclick()