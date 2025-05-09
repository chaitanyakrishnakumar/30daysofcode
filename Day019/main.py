from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="which turtle will win the race? Enter a color: ")
colors = ["red","plum", "gold","blue", "green", "purple"]
all_turtles = []

coordinates = [-230,-90]
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.speed(3)
    new_turtle.goto(x=coordinates[0], y=coordinates[1])
    coordinates[1] += 30
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! the {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost. the {winning_color} turtle is the winner!")

            random_distance = random.randint(0,10)
            turtle.forward(random_distance)
screen.exitonclick()
