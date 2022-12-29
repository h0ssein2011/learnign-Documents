from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

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
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    
    # detect collosion with paddle
    if (ball.distance(r_paddle) < 50 or ball.xcor() >320) or (ball.distance(l_paddle) < 50 or ball.xcor() < -320):
        ball.bounce_x()
    
    # paadle missed the ball

    if (ball.distance(r_paddle) > 50 and ball.xcor() > 320) :
        print('ball missed')
        ball.home()

    
    # print(ball.xcor() , ball.ycor()) 
    

        
    

  


  

        


screen.exitonclick()