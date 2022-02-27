from Car import Car
class Carpark:

    def __init__(self, capacity):
        self.spaces = []
        self.capacity = capacity
        self.reg = []

    def add_car(self, Car):
        if len(self.spaces) < self.capacity and Car.model == "Car" and not self.is_duplicate(Car.reg):
            self.spaces.append(Car)


    def is_duplicate(self, reg_num):
        for Car in self.spaces:
            if Car in self.spaces:
                if

