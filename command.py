import unittest
from hotel.daterange import DateRange
from hotel.guest import Guest
from hotel.hotel import Hotel
from hotel.reservation import Reservation
from collections import OrderedDict
import json
end = "\n"
hotel = Hotel("durham", "./Rooms.json")

# This is the command line script, it runs an infinite loop that prompts for input and runs code based on the input.
# most of the work is done by the hotel and this directs the variables into it

class Command:

    def __init__(self):
            self.running = False
            self.command_list = """
exit : exits the command line add guest: adds a new guest using user details \n
find guest: finds an existing guest, find room: finds a room within the hotel \n
all rooms: prints all rooms in the hotel, create reservation: creates a reservation using user details \n
find reservation: finds an exsiting reservation, cancel reservation: removes an existing reservation
"""

# FIX GOOF WHERE INPUTING SOMEHTING OTHER THAN A REGISTERD COMMAND THROWS AN ERROR EX: >> 1 = error
# PRINT OUT RESERVATIONS IN PRETTY WAY

    def run(self):
        # Starts a while loop that loops while 'running' is True
        self.running = True
        # Looks through all of the commands to find the one that matches the input
        if self.running == True :
            while self.running == True:
                val = input(">> ") 
                if "exit" in val:
                    self.quit()
                elif "help" in val:
                    self.help()
                elif "add guest" in val:
                    self.add_new_guest()
                elif "find guest" in val:
                    self.find_guest()
                elif "find room" in val:
                    self.find_room()
                elif "all rooms" in val:
                    self.print_all_rooms()
                elif "create reservation" in val:
                    self.create_reservation()
                elif "find reservation" in val:
                    self.find_reservation()
                elif "cancel reservation" in val:
                    self.cancel_reservation()
                else :
                    print("'" + val + "'" + " is not a command")
        
    def quit(self):
        # exits the infinite loop by changine 'running' to False
        self.running = False
        return self.running

    def help(self):
        # lists out all of the commands that are usable
        print(self.command_list)

    def add_new_guest(self):
        # uses user input to assign the variables needed to run hotel.add_guest
        name = input("name:")
        credit_card = input("credit card number:")
        phone_num = input("phone number:")
        guest = hotel.add_guest(name, credit_card, phone_num)
        print("guest created :", guest)

    def find_guest(self):
        # uses user input to decide what criteria to look for a guest under
        choice = input("find by [id, name, phone]: ")
        # takes user input to find the guest using hotel.find_guests
        if choice == "id":
            id = input("id :")
            the_list = hotel.find_guests({"id" : id})
        if choice == "name":
            name = input("name :")
            the_list = hotel.find_guests({"name" : name})
        if choice == "phone":
            phone_number = input("phone :")
            the_list = hotel.find_guests({"phone" : phone_number})

        hotel.print_list(the_list)
        
    def find_room(self):
        # finds a room that best matches the criteria given
        floor = input("prefered floor [1 - 3]: ")
        view = input("prefered view level [good, decent, poor]: ")
        bedNum = input("prefered number of beds[1 ,2]: ")

        matching_rooms = hotel.all_rooms_check(view, int(floor), int(bedNum))
        print(matching_rooms)
    
    def print_all_rooms(self):
        hotel.print_all_rooms()

    def create_reservation(self):
        guest_name = input("guest name: ")
        view_level = input("prefered view level [good, decent, poor]: ")
        floor = int(input("prefered floor [1 - 3]: "))
        desired_bed_num = int(input("prefered number of beds[1 ,2]: "))
        start_date = input("start date of stay[yyyy-mm-dd]: ")
        end_date = input("end date of stay[yyyy-mm-dd]: ")

        # creates a new reservation object with the input given
        new_res = hotel.create_res(guest_name, view_level, floor, desired_bed_num, start_date, end_date)

    def find_reservation(self):
        # has a nested while loop that checks to make sure what has been inputed matches what is expected
        running = True

        while running:
            choice = input("find by[id, name, start date]: ")

            if choice == "id":
                id = input("id: ")
                the_list = hotel.find_res({"id" : id})
            if choice == "name":
                name = input("guest name: ")
                the_list = hotel.find_res({"name" : name})
            if choice == "start date":
                start_date = input("start date: ")
                the_list = hotel.find_res({"start date" : start_date})
            if not (choice == "id" or choice == "name" or choice == "start date"):
                # prints an error message if it doesn't match and gives the input option again
                print("'"+choice+"' is not an option:")
            else :
                running = False

        hotel.print_list(the_list)

    def cancel_reservation(self):
        #deletes a reservation based on id
        id = input("reservation id: ")
        hotel.cancel_res(id)

# starts the command loop when the file is run
cmd = Command()
cmd.run()