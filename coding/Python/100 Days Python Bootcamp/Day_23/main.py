import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move_forward, "Up")


car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    # check if Player reached the top screen
    if player.ycor() > 280 :
        score_board.update_score_baord()
        score_board.show_score()
        player.reset_player()
        # car_manager.car_list[0].move_speed *= 0.9
    
    # detect collision with car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()



    



    
    
    
        



screen.exitonclick()