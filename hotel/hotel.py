import json

from collections import OrderedDict

from hotel.guest import Guest

from hotel.daterange import DateRange

from hotel.reservation import Reservation

class Hotel:
    def __init__(self, location, room_directory):
        with open(room_directory) as maui_rooms_list:
            data = maui_rooms_list.read()
            maui_rooms_list = json.loads(data)
            
        self.location = location
        self.room_dict = maui_rooms_list
        self.guest_dict = OrderedDict()
        self.id_dict = []
        self.res_dict = {}
        self.next_guest_id = 0
        self.next_res_id = 0

    
    def check_if_in_use(self, room, start, end):
    # returns rooms that don't overlap to use when creating reservations
        bad_list = []
        

        if self.res_dict != 0:
            for res in self.res_dict.values():

                overlap_1 = res.start <= start and start <= res.end 
                overlap_2 = start <= res.start and res.start <= end

                if str(room) in str(res.room_num):

                    if overlap_1 or overlap_2:
                        bad_list.append(res)

        if len(bad_list) == 0:
            return True
        
        else :
            return False

    def new_guest_id(self):
        self.next_guest_id += 1
        return "guest-" + str(self.next_guest_id)

    def add_guest(self, name, card_num, phone_num):
        id = self.new_guest_id()

        #create the new guest in the Guest class
        new_guest = Guest(name, id, card_num, phone_num)

        #creates the dictionary object with the new id as the key
        self.guest_dict[id] = new_guest

        return new_guest

    def find_guest_by_id(self, id):
        guest_list = self.find_guests({"id": id})
        if len(guest_list) == 1:
            return guest_list[0]
        else:
            return None

    # uses a dictionary as the arguement in this function, looks for the key in the dictionary, if none uses DEFAULT ARGUEMENT
    # finds guest based on either id, name or phone number
    def find_guests(self, search = False):
        guests_list = []

        if search == False:
            for guest in self.guest_dict.values():
                guests_list.append(guest)
        else : 
            for id, guest in self.guest_dict.items():
                if "id" in search:
                    if search["id"] == id:
                        guests_list.append(guest)

                if "name" in search:
                    if search["name"] == guest.name:
                        if not guest in guests_list:
                            guests_list.append(guest)

                if "phone" in search:
                    if search["phone"] == guest.phone_num:
                        if not guest in guests_list:
                            guests_list.append(guest)
        return guests_list
                
    def print_list(self, the_list):
        # objects that are passed in need the __str__() finction otherwise <object.foo12345> will be printed
        if len(the_list) == 0:
            print("nothing matches the search")
        else:
            for elem in the_list:
                print(elem) 

    def print_all_rooms(self):
        for room in self.room_dict["rooms"]:
            print(room)

    
    def all_rooms_check(self, view_level, floor, desired_bed_num):
        # attempts to find the best possible room to fit criteria given
        match_list = []

        # starts by looking for a perfect match
        for room in self.room_dict["rooms"]:
            if room["view"] == view_level and str(room["roomNum"])[0] == str(floor) and desired_bed_num == room["numOfBeds"]:
                match_list.append(room["roomNum"])
            
        for room in self.room_dict["rooms"]:
            if room["numOfBeds"] == desired_bed_num and str(room["roomNum"])[0] == str(floor):
                match_list.append(room["roomNum"])
            else :
                if room["numOfBeds"] == desired_bed_num:
                    match_list.append(room["roomNum"])

        # an error is thrown if there is not a singe room that has the right number of beds
        if len(match_list) == 0:
            match_list.append("there are no available rooms that match the search")

        return match_list

    def new_res_id(self):
        self.next_res_id += 1
        return "res-" + str(self.next_res_id)
                
    def create_res(self, guest_name, view_level, floor, desired_bed_num, start_date, end_date):
        # this creates a new reservation object and gets its name/view/floor/etc off of the input in command script
        res_list = []
        good_room_list = []

        id = self.new_res_id()

        room_list = self.all_rooms_check(view_level, floor, desired_bed_num)

        if not type(room_list[0]) == str:
            for room in room_list:
                
                if self.check_if_in_use(int(room), start_date, end_date):
                    good_room_list.append(room)

            new_res = Reservation(guest_name, id, int(good_room_list[0]), start_date, end_date)
            self.res_dict[id] = new_res

        else :
            return "failed to create res"


    def find_res(self, search = False):
        res_list = []
        # uses default arguement if nothing is inputted and prints all reservations, otherwise it finds the reservation
        # based on the criteria given in the command line script
        if search == False:
            for res in self.res_dict.values():
                res_list.append(res)
        else : 
            for id, res in self.res_dict.items():
                if "id" in search:
                    if search["id"] == id:
                        res_list.append(res)

                if "name" in search:
                    if search["name"] == res.occupant:
                        if not res in res_list:
                            res_list.append(res)

                if "start date" in search:
                    if search["start date"] == res.start:
                        if not res in res_list:
                            res_list.append(res)

        return res_list

    def find_res_by_id(self, id):
        res_list = self.find_res({"id": id})
        if len(res_list) != 0:
            return res_list[0]
        else:
            return None

    def cancel_res(self, id):
        del self.res_dict[id]