from vehicle import Motorcycle, Car, Truck 
from parkingspot import ParkingSpot as pk
from parking_manager import ParkingManager as pm

def main():

    physical_spots = [
        pk(spot = "C1", size ="Small"),
        pk(spot = "C2", size ="Small"),
        pk(spot = "L1", size="Large"),
    ]

    manager = pm(physical_spots)


    v1 = Motorcycle(license = "FARTS")  
    v2 = Truck(license = "STINK")       
    v3 = Car(license = "ALOT")
    v4 = Motorcycle(license = "YEP")


    manager.parkVehicle(v1)
    manager.parkVehicle(v2)
    manager.parkVehicle(v3)
    manager.parkVehicle(v4)


    







if __name__ == "__main__":
    main()