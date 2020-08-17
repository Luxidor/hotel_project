import json

from collections import OrderedDict

from hotel.guest import Guest

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
        self.res_dict = OrderedDict()
        self.next_guest_id = 0
        self.next_res_id = 0

    def new_guest_id(self):
        self.next_guest_id += 1
        return "guest-" + str(self.next_guest_id)

    def add_guest(self, name, card_num, phone_num):
        id = self.new_guest_id()

        #create the new guest in the Guest class
        new_guest = Guest(name, id, card_num, phone_num)

        self.guest_dict[id] = new_guest

        return new_guest

    def find_guest_by_id(self, id):
        guest_list = self.find_guests({"id": id})
        if len(guest_list) == 1:
            return guest_list[0]
        else:
            return null

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
                
    # only works if the objects that are passed in have the __str__() finction
    def print_list(self, the_list):
        if len(the_list) == 0:
            print("nothing matches the search")
        else:
            for elem in the_list:
                print(elem)

    
    def all_rooms_check(self, view_level, floor, desired_bed_num):
        match_list = []
        for room in self.room_dict["rooms"]:
            if room["view"] == view_level and str(room["roomNum"])[0] == str(floor) and desired_bed_num == room["numOfBeds"]:
                match_list.append(room["roomNum"])
            
        if len(match_list) == 0:
            for room in self.room_dict["rooms"]:
                if room["numOfBeds"] == desired_bed_num and str(room["roomNum"])[0] == str(floor):
                    match_list.append(room["roomNum"])
                else :
                    if room["numOfBeds"] == desired_bed_num:
                        match_list.append(room["roomNum"])
                    else :
                        if not "there are no available rooms that match the search" in match_list and len(match_list) == 0:
                            match_list.append("there are no available rooms that match the search")
        
        for room in match_list:
            self.check_if_in_use(room)

        return match_list

    def new_res_id(self):
        self.next_res_id += 1
        return "res-" + str(self.next_res_id)
                
    def create_res(self, guest_name, view_level, floor, desired_bed_num, start_date, end_date):

        res_list = []

        matching_rooms = self.all_rooms_check(view_level, floor, desired_bed_num)

        if not matching_rooms[0] == str:
            res_room_num = matching_rooms[0]

            new_res = Reservation(guest_name, res_room_num, start_date, end_date)
            id = self.new_res_id()

            self.res_dict[id] = new_res

        else :
            print(matching_rooms)

    def find_res_by_id(self, id):
        res_list = self.find_res({"id": id})
        if len(res_list) == 1:
            return res_list[0]
        else:
            return null

    def find_res(self, search = False):
        res_list = []

        if search == False:
            for res in self.res_dict.values():
                res_list.append(res)
        else : 
            for id, res in self.res_dict.items():
                if "id" in search:
                    if search["id"] == id:
                        res_list.append(res)

                if "name" in search:
                    if search["name"] == res.name:
                        if not res in res_list:
                            res_list.append(res)

                if "start date" in search:
                    if search["start date"] == res.phone_num:
                        if not res in res_list:
                            res_list.append(res)

        return res_list

        def check_if_in_use(self, room):
        # returns rooms that overlap
            overlap_list = []

            for res in res_dict:
                if room.room_num == room:
                    overlap_list.append(room)