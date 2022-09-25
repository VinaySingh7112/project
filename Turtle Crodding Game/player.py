from turtle import Turtle

from numpy import True_
 

STARTING_POSITION=(0,-280)
MOVE_DISTENCE=10
FENESH_LINE_Y=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        


    def go_up(self):
        self.forward(MOVE_DISTENCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > FENESH_LINE_Y:
            return True
        else:
            return False
