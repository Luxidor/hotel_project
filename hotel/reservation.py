from hotel.daterange import DateRange

# Primarily this class just stores data about reservations

class Reservation :
    def __init__ (self, occupant, id, room_num, start, end):
        self.id = id
        self.occupant = occupant 
        self.room_num = room_num
        self.start = start
        self.end = end
        self.date_range = (start, end)

    def __str__(self):
        occ = str(self.occupant)
        id = str(self.id)
        room = str(self.room_num)
        st = str(self.start)
        end = str(self.end)
        return ("name: " + occ + ", room number: " + room + ", start date: " + st + ", end date: " + end + ", id: " + id)
        
    def display_summary(self):
        print(self.occupant + ' is in room # ' + str(self.room_num) + " " + self.date_range.to_display())

