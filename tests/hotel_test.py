import unittest
from hotel.daterange import DateRange
from hotel.guest import Guest
from hotel.hotel import Hotel
from hotel.reservation import Reservation
from collections import OrderedDict
import json

class HotelTest(unittest.TestCase):
    "testing the hotel's management of guests and reservations"

    def create_hotel(self):
        hotel = Hotel("durham", "/Users/23morrisc/code/HotelProject/Rooms.json")
        return hotel

    def test_storing_guests(self):
        "should create and store a new guest object"
        guest_1 = Guest("bob", "guest-1", "1234 1235 1236 1237", "(098) 765-4321")

        self.assertEqual(guest_1.id, "guest-1")
        
    def test_creating_id(self):
        "should create new guest id"
        hotel = self.create_hotel()
        hotel.new_guest_id()
        hotel.new_guest_id()
        hotel.new_guest_id()
        self.assertEqual(hotel.new_guest_id(), "guest-4")


    def test_creating_guest(self):
        "creates a guest using the add_guest() function and finds the guest by id"
        hotel = self.create_hotel()

        hotel.add_guest("billy bob joe", "1234 1234 1234 1234", "123 456 7890")
        
        self.assertEqual(hotel.find_guest_by_id("guest-1").name, "billy bob joe")

    def test_finding_guest_by_name(self):
        hotel = self.create_hotel()

        hotel.add_guest("jim", "1234 5468 4322 8743", "9899999090")
        guest_list = hotel.find_guests({"name" : "jim"})

        self.assertEqual(guest_list[0].name, "jim")

    def test_finding_guest_by_phoneNum(self):
        hotel = self.create_hotel()

        hotel.add_guest("jim", "1234 5468 4322 8743", "(890) 890 8900")
        guest_list = hotel.find_guests({"phone" : "(890) 890 8900"})

        self.assertEqual(guest_list[0].phone_num, "(890) 890 8900")

    def test_finding_all_guests(self):
        hotel = self.create_hotel()
        hotel.add_guest("jim", "1234 5468 4322 8743", "(890) 890 8900")
        hotel.add_guest("billy bob joe", "1233 1234 1234 1234", "123 426 7890")
        hotel.add_guest("billy bob jim", "1237 1234 1234 1234", "123 486 7890")
        hotel.add_guest("billy bob jozie", "1934 1234 1234 1234", "123 456 7890")

        guest_list = hotel.find_guests()

        self.assertEqual(4, len(guest_list))

    def test_finding_rooms(self):
        "should find a room with a poor view level on floor 1 with 2 beds"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("poor", 1, 2)

        self.assertTrue(match_list[0] == 101)

    def test_finding_rooms2(self):
        "should find a room with a decent view on floor 2 with 1 bed"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("decent", 2, 1)

        self.assertTrue(match_list[0] == 202)

    def test_finding_rooms3(self):
        "should find a room with a good view on floor 3 with 2 beds"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("good", 3, 2)

        self.assertTrue(match_list[0] == 315)

    def test_finding_meh_rooms(self):
        "should find all of the rooms that only match the bed num"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("good", 2, 2)

        self.assertTrue(len(match_list) == 2)

    def test_finding_meh_rooms2(self):
        "should find the room(s) that has both 2 beds and is on floor one"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("decent", 1, 2)

        self.assertTrue(match_list[0] == 101)

    def test_no_matching_rooms(self):
        "should print the thingy about no rooms matching the search"
        hotel = self.create_hotel()

        match_list = hotel.all_rooms_check("good", 1, 3)

        self.assertTrue(match_list[0] == "there are no available rooms that match the search")

    def test_no_available_rooms_for_search(self):
        "should see that there is a room that matches the search but it is unavaiable"
        hotel = self.create_hotel()

        self.assertTrue(match_list[0] == "there are no available rooms that match the search")

    def test_storing_reservations(self):
        "should store a new res"
        hotel = self.create_hotel()

        res_1 = Reservation("bob", 123, "startDate", "endDate")

        self.assertTrue(res_1.occupant == "bob")

    def test_creating_res_ids(self):
        "should create a new id for res"
        hotel = self.create_hotel()

        hotel.new_res_id()
        hotel.new_res_id()
        hotel.new_res_id()

        self.assertTrue(hotel.new_res_id() == "res-4")

    def test_creating_reservation(self):
        "should create reservations"
        hotel = self.create_hotel()

        hotel.create_res("bob", 2, "poor", 1)