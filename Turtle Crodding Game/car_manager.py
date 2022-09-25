from turtle import Turtle
import random

from numpy import square

COLORS=["red","green","yellow","blue","black","orange"]
STARTING_MOVE_DISTENCE=5
MOVE_INCREMENT=10

class carManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTENCE


    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_cars=Turtle("square")
            new_cars.shapesize(stretch_wid=1,stretch_len=2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_cars.goto(300,random_y)
            self.all_cars.append(new_cars)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    

    def lavel_up(self):
        self.car_speed  +=MOVE_INCREMENT


    