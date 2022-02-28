from Vehicle import Vehicle


class Carpark:

    def __init__(self, capacity):
        self.spaces = []
        self.capacity = capacity
        self.reg = []

    def add_car(self, Vehicle):
        if len(self.spaces) < self.capacity and Vehicle.type == "Car" and not self.is_duplicate(Vehicle.reg):
            self.spaces.append(Vehicle)

    def is_duplicate(self, Vehicle):
        for reg in self.reg:
            if Vehicle.reg == reg:
                return "CALL THE POLICE!"


