from vehicle import Motorcycle, Car, Truck 
from parkingspot import ParkingSpot as pk
from parking_manager import ParkingManager as pm

def main():

    physical_spots = [
        pk(spot = "C1", size ="Small"),
        pk(spot = "C2", size ="Small"),
        pk(spot = "L1", size="Large"),
        pk(spot = "M1", size = "Medium")
    ]

    manager = pm(physical_spots)


    v1 = Motorcycle(license = "FARTS")  
    v2 = Truck(license = "STINK")       
    v3 = Car(license = "ALOT")
    v4 = Motorcycle(license = "YEP")



    v1_ticket = manager.parkVehicle(v1)
    v2_ticket = manager.parkVehicle(v2)
    v3_ticket = manager.parkVehicle(v3)
    v4_ticket = manager.parkVehicle(v4)





    







if __name__ == "__main__":
    main()