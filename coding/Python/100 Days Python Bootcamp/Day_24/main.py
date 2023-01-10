import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Snake Game")

snake = Snake()
Food = Food()

screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    
    # detect collisions with wall
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        game_is_on = False

    # detect collision with snake
    if snake.distance(Food) < 15:
        # game_is_on = False
        print('Collision with Food')




screen.exitonclick()