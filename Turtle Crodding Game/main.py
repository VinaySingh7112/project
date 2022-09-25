import time
from turtle import Screen
from player import Player
from car_manager import carManager
from scoreboard import Scoreboard

screen=Screen()
player=Player()
car_manager=carManager()
scoreboard=Scoreboard()


screen.setup(width=600,height=600)
screen.tracer()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


     #Detcet collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    #Detcet successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.lavel_up()   
        scoreboard.increase_level()     

screen.exitonclick()