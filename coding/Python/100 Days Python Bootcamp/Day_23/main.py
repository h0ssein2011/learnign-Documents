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



wait_time = 0
car_list = []
car_list.append(CarManager())
car_list.append(CarManager())


game_is_on = True
while game_is_on:
    time.sleep(car_list[0].move_speed)
    screen.update()
    wait_time += 0.1
    #every 1 seconds a new car is added to the screen
    if wait_time > 3:
        wait_time = 0
        new_car = CarManager()
        car_list.append(new_car)
    # move a random car in every 0.1 seconds
    ready_car =random.randint(1, len(car_list)-1)
    car_list[ready_car].move_car()

    # check if Player reached the top screen
    if player.ycor() > 280 :
        score_board.update_score_baord()
        score_board.show_score()
        player.reset_player()
        car_list[0].move_speed *= 0.9
    
    # detect collision with car
    for car in car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()



    



    
    
    
        



screen.exitonclick()