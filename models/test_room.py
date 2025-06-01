import unittest
from hotel_reservation_system.models.room import Room

class TestRoom(unittest.TestCase):
    def test_valid_room_creation(self):
        room = Room("101", "double", 350.0, 2)
        self.assertEqual(room.number, "101")
        self.assertEqual(room.room_type, "double")
        self.assertEqual(room.price_per_night, 350.0)
        self.assertEqual(room.capacity, 2)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            Room("", "double", 350.0, 2)

    def test_invalid_room_type(self):
        with self.assertRaises(ValueError):
            Room("101", "", 350.0, 2)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Room("101", "double", -50, 2)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            Room("101", "double", 350.0, 0)

    def test_get_details(self):
        room = Room("102", "single", 200.0, 1)
        details = room.get_details()
        expected = {
            "number": "102",
            "room_type": "single",
            "price_per_night": 200.0,
            "capacity": 1
        }
        self.assertEqual(details, expected)

    def test_str_representation(self):
        room = Room("103", "suite", 500.0, 3)
        expected = "Room 103 (suite, Capacity: 3, Price: $500.00/night)"
        self.assertEqual(str(room), expected)

    def test_repr_representation(self):
        room = Room("104", "single", 150.0, 1)
        expected = "Room(number='104', room_type='single', price_per_night=150.0, capacity=1)"
        self.assertEqual(repr(room), expected)

#if __name__ == "__main__":
#   unittest.main()
