from hotel.daterange import DateRange

class Reservation :
    def __init__ (self, occupant, room_num, start_date, end_date):
        self.occupant = occupant 
        self.room_num = room_num
        self.start_date = start_date
        self.end_date = end_date
        self.date_range = (start_date, end_date)
        
    def display_summary(self):
        print(self.occupant + ' is in room # ' + str(self.room_num) + " " + self.date_range.to_display())

    def change_room(self, new_room):
        self.room_num = new_room

    def delete_res(self):
        pass
        # delete a person's reservation

