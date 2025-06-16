import unittest
from models.room import Room

class TestRoom(unittest.TestCase):

    def test_poprawne_utworzenie_pokoju(self):
        pokoj = Room("101", "dwuosobowy", 250.0, 2)
        self.assertEqual(pokoj.number, "101")
        self.assertEqual(pokoj.room_type, "dwuosobowy")
        self.assertEqual(pokoj.price_per_night, 250.0)
        self.assertEqual(pokoj.capacity, 2)

    def test_nieprawidlowy_numer_pokoju(self):
        with self.assertRaises(ValueError):
            Room("", "dwuosobowy", 250.0, 2)
        with self.assertRaises(ValueError):
            Room(None, "dwuosobowy", 250.0, 2)

    def test_nieprawidlowy_typ_pokoju(self):
        with self.assertRaises(ValueError):
            Room("101", "", 250.0, 2)
        with self.assertRaises(ValueError):
            Room("101", None, 250.0, 2)

    def test_nieprawidlowa_cena(self):
        with self.assertRaises(ValueError):
            Room("101", "dwuosobowy", -100.0, 2)
        with self.assertRaises(ValueError):
            Room("101", "dwuosobowy", "za darmo", 2)

    def test_nieprawidlowa_pojemnosc(self):
        with self.assertRaises(ValueError):
            Room("101", "dwuosobowy", 250.0, 0)
        with self.assertRaises(ValueError):
            Room("101", "dwuosobowy", 250.0, -1)
        with self.assertRaises(ValueError):
            Room("101", "dwuosobowy", 250.0, "dwie osoby")

    def test_szczegoly_pokoju(self):
        pokoj = Room("202", "apartament", 400.0, 3)
        oczekiwane = {
            "numer": "202",
            "typ_pokoju": "apartament",
            "cena_za_noc": 400.0,
            "pojemnosc": 3
        }
        self.assertEqual(pokoj.get_details(), oczekiwane)

    def test_str_i_repr(self):
        pokoj = Room("303", "jednoosobowy", 180.0, 1)
        self.assertEqual(str(pokoj), "Pokój: 303 (jednoosobowy), 1 os., 180.00 zł/noc")
        self.assertIn("Pokój(numer='303'", repr(pokoj))

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
