from parkingspot import ParkingSpot as pk
import vehicle

class ParkingManager:
    def __init__(self, list_spots: list):
        
        self.available_spots = {"Medium" : [], "Large" : [], "Small" : []}
        self.active_assignments = {}


        for spot in list_spots:
            self.available_spots[spot.get_size()].append(spot) 
    


    def parkVehicle(self, vehicle):
        v_type = vehicle.get_size()

        if self.available_spots[v_type]:

            assigned_spot = self.available_spots[v_type].pop(0)

            assigned_spot.occupy(vehicle)

            self.active_assignments[vehicle.get_license_plate()] = assigned_spot

            print(f"Vehicle {vehicle.get_license_plate()} has sucessfully parked in spot: {assigned_spot.get_spot()}")

            return assigned_spot.get_spot
        else:
            print(f"Unable to park in {v_type} spots; Full")

            return None

