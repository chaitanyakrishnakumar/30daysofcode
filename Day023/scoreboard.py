from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.goto(-290,270)
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f"Level {self.level}", align="left", font=FONT)
        
    def level_up(self):
        self.level += 1
        self.display()

     def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)
        
