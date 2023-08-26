import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.onkeypress(player.move_up, "w")
    car_manager.create_cars()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_finished():
        player.go_starting()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()
