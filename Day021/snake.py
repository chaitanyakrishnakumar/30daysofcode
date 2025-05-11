from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_block(position)

    def add_block(self,position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.blocks.append(new_turtle)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):  # range(start=len(segments)-1,stop=0,step=-1):
            new_x = self.blocks[block - 1].xcor()
            new_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
         if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
