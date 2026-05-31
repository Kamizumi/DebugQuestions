class Vehicle:

    def __init__(self, license, size):

        self.__license = license
        self.size = size
    
    def get_license_plate(self):
        return self.__license
    
    def get_size(self):
        return self.size

class Motorcycle(Vehicle):
    def __init__(self, license):
        super().__init__(license, size = "small")


class Truck(Vehicle):
    def __init__(self,license):
        super().__init__(license, size = "large")

class Car(Vehicle):
    def __init__(self, license):
        super().__init__(license, size = "medium")
