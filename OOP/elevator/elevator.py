import time

class Elevator:

    def __init__(self, max_weight : int, max_floor : int, min_floor : int, elevator_id : str, door_closed = True, buttons_pressed = None):

        self.direction = "IDLE"
        self.curr_weight = 0
        self.passenger_count = 0

        self.max_weight = max_weight
        self.max_floor = max_floor
        self.min_floor = min_floor
        self.curr_floor = min_floor
        self.elevator_id = elevator_id
        self.door_closed = door_closed
        
        if buttons_pressed is None:
            self.buttons_pressed = []
        else:
            self.buttons_pressed = buttons_pressed
    
    def open(self):
        self.door_closed = False
    
    def close(self):
        self.door_closed = True
    
    def go_to_floor(self, floor : int):

        if floor > self.max_floor or floor < self.min_floor:
            print(f"Invalid floor request")
            return
        
        direction = "UP" if floor > self.curr_floor else "DOWN"

        while self.curr_floor != floor:
            if direction == "UP":
                self.curr_floor += 1
            else:
                self.curr_floor -= 1
            print(f"Elevator: {self.elevator_id} is currently at floor {self.curr_floor} ")

        self.direction = "IDLE"
        self.open()
        self.close()

    
    def passenger_boards(self, ps_weight : int):
        self.open()
        if self.curr_weight + ps_weight > self.max_weight:
            print("MAXIMUM WEIGHT CAPACITY EXCEEDED. ONE PERSON MUST EXIT")
            self.close()
            return False

        self.curr_weight += ps_weight
        self.passenger_count += 1
        print("Successfully boarded")
        self.close()
        return True
    
    def passenger_exits(self, ps_weight : int):
        self.open()
        self.curr_weight -= ps_weight
        self.passenger_count -= 1
        self.close()


class Request:
    def __init__(self, curr_floor: int, destination_floor : int, direction: str):
        self.curr_floor = curr_floor
        self.destination_floor = destination_floor
        
        if destination_floor > curr_floor:
            self.direction = "UP"
        elif destination_floor < curr_floor:
            self.direction = "DOWN"
        else:
            self.direction = "IDLE"

class Dispatcher:
    def __init__(self, elevators : list):
        self.elevators = elevators
    

    def handle_requests(self, request : Request):
        print(f"Processing request: {request.curr_floor} to {request.destination_floor}")

        chosen_elevator = None

        distance = float('inf')

        for elevator in self.elevators:
            
            curr_distance = abs(request.curr_floor - elevator.curr_floor)

            if curr_distance < distance:
                distance = curr_distance
                chosen_elevator = elevator
        
        if chosen_elevator:
            chosen_elevator.go_to_floor(request.curr_floor)
            chosen_elevator.go_to_floor(request.destination_floor)



def main():
    elevator_one = Elevator(max_weight = 2500, max_floor = 50, min_floor = 1, elevator_id = "INEEDAJOB")
    elevator_two = Elevator(max_weight = 1500, max_floor = 50, min_floor = 1, elevator_id = "PIXELMONISFUN")
    
    elevator_one.curr_floor = 23
    elevator_two.curr_floor = 2
    
    elevator_operator = Dispatcher([elevator_one, elevator_two])

    user_request = Request(curr_floor = 35, destination_floor = 50, direction = "UP")

    elevator_operator.handle_requests(user_request)




if __name__ == "__main__":
    main()




    

