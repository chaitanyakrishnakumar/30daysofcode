import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
turtle = Player()
screen.onkeypress(turtle.move, "space")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.display()
    car_manager.create_car()
    car_manager.move()

    # Detect turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    # Detect successful crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
