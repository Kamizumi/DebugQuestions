from vehicle import Vehicle, Motorcycle, Car, Truck
class ParkingSpot:

    def __init__(self, spot: str, size: str):

        self.spot = spot
        self.size = size
        self.Vehicle = None
    
    def is_available(self):
        return self.Vehicle is None
    
    def vacate(self):
        self.Vehicle = None
    
    def occupy(self, vehicle):
        self.Vehicle = vehicle
    
    def get_spot(self):
        return self.spot

    def get_size(self):
        return self.size
