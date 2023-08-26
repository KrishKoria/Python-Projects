from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_cars(self):
        if random.randint(1, 4) == 1:
            new_car = Turtle("square")
            new_car.pu()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(400, random.randint(-320, 340))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5
