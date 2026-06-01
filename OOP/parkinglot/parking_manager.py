from parkingspot import ParkingSpot as pk
import vehicle
from ticket import Ticket as tk

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
            
            new_ticket = tk(vehicle, assigned_spot)

            self.active_assignments[new_ticket.get_ticket] = new_ticket

            print(f"Vehicle {vehicle.get_license_plate()} has sucessfully parked in spot: {assigned_spot.get_spot()}.")
            print(f"Your ticket for {vehicle.get_license_plate()} is {new_ticket.get_ticket()}\n")

            return new_ticket
        else:
            print(f"Unable to park in {v_type} spots; Full\n")

            return None

