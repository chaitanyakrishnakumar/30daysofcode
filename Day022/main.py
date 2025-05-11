import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(height=600, width= 800)
screen.title("pong game")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350,0))
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")

l_paddle = Paddle((-350,0))
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

ball = Ball()
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    # Detect collision to walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle miss
    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()

    # detect l_paddle miss
    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()
