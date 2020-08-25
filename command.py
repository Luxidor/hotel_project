import unittest
from hotel.daterange import DateRange
from hotel.guest import Guest
from hotel.hotel import Hotel
from hotel.reservation import Reservation
from collections import OrderedDict
import json

hotel = Hotel("durham", "/Users/23morrisc/code/hotel_project/Rooms.json")

class Command:

    def __init__(self):
            self.running = False
            self.command_list = ["exit : exits the command line", "add guest: adds a new guest"]

    def run(self):

        self.running = True

        if self.running == True :
            while self.running == True:
                val = input(">> ") 
                if "exit" in val:
                    self.quit()
                if "help" in val:
                    self.help()
                if "add guest" in val:
                    self.add_new_guest()
                if "find guest" in val:
                    self.find_guest()
                if "find room" in val:
                    self.find_room()
                if "all rooms" in val:
                    self.print_all_rooms()
                if "create reservation" in val:
                    self.create_reservation()
                if "find reservation" in val:
                    self.find_reservation()
                if "cancel reservation" in val:
                    self.cancel_reservation()
        
    def quit(self):
        self.running = False
        return self.running

    def help(self):
        print(self.command_list)

    def add_new_guest(self):
        name = input("name:")
        credit_card = input("credit card number:")
        phone_num = input("phone number:")
        guest = hotel.add_guest(name, credit_card, phone_num)
        print("guest created :", guest)

    def find_guest(self):
        choice = input("find by [id, name, phone] :")

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
        pass
    
    def print_all_rooms(self):
        pass

    def create_reservation(self):
        pass

    def find_reservation(self):
        pass

    def cancel_reservation(self):
        pass


cmd = Command()
cmd.run()