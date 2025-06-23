import unittest
from unittest.mock import patch
from datetime import date, timedelta

from main import (
    hotel, guests, guest_reservations, payments, add_room,
    register_guest, make_reservation, confirm_payment
)

class TestIntegracyjnyRezerwacja(unittest.TestCase):
    @patch('builtins.input')
    def test_rezerwacja_i_platnosc(self, mock_input):
        dzisiaj = date.today()
        jutro = dzisiaj + timedelta(days=1)

        dane_wejsciowe = [
            "100",
            "single",
            "200",
            "1",
            "Jan",
            "Kowalski",
            "jankowalski@email.com",
            "123456789"
        ]

        mock_input.side_effect = dane_wejsciowe
        add_room()
        self.assertEqual(len(hotel.get_all_rooms()), 1)

        register_guest()
        self.assertEqual(len(guests), 1)

        lista_gosci = list(guests.keys())
        gosc_id = lista_gosci[0]

        mock_input.side_effect = [
            gosc_id,
            dzisiaj.strftime("%Y-%m-%d"),
            jutro.strftime("%Y-%m-%d"),
            "100",
            "karta"
        ]

        make_reservation()
        self.assertEqual(len(hotel.get_all_reservations()), 1)

        self.assertEqual(len(payments), 1)
        lista_platnosci = list(payments.values())
        platnosc = lista_platnosci[0]
        self.assertFalse(platnosc.paid)

        mock_input.side_effect = [platnosc.payment_id]
        confirm_payment()
        self.assertTrue(platnosc.paid)

if __name__ == '__main__':
    unittest.main()

