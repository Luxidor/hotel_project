from hotel.daterange import DateRange

class Reservation :
    def __init__ (self, occupant, room_num, start, end):
        self.occupant = occupant 
        self.room_num = room_num
        self.start_date = start_date
        self.end_date = end_date
        self.date_range = (start, end)
        
    def display_summary(self):
        print(self.occupant + ' is in room # ' + str(self.room_num) + " " + self.date_range.to_display())

    def change_room(self, new_room):
        self.room_num = new_room

    def delete_res(self):
        pass
        # delete a person's reservation

    def does_overlap(self, room, start_date, end_date):
        if not self.room_num == room:
            return False
        else :
            if self.start <= start_date and start_date <= self.end or start_date <= self.start and self.start <= end_date:
                return True

