import uuid
from datetime import datetime
class Ticket:

    def __init__(self, vehicle, spot):

        self.spot = spot
        self.vehicle = vehicle

        self.__ticket_id =  str(uuid.uuid4())[:8]
        self.__entry_time = datetime.now()
        self.is_paid = False
    

    def get_ticket(self):
        return self.__ticket_id
    

    def calcParkDuration(self):

        duration = datetime.now() - self.__entry_time

        return duration.total_seconds / 3600
