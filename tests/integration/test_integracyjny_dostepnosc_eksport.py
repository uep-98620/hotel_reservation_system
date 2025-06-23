import unittest
from unittest.mock import patch
from datetime import date, timedelta
import os

from main import (
    add_room, make_reservation, guests, guest_reservations, payments, hotel, check_guest_room, show_room_reservations,
    show_guest_payments, export_reservations_to_csv, show_available_rooms, register_guest, confirm_payment
)

class TestIntegracyjnyDostepnoscEksport(unittest.TestCase):
    @patch('builtins.input')
    def test_dostepnosc_eksport(self, mock_input):
        dzisiaj = date.today()
        jutro = dzisiaj + timedelta(days=1)

        dane_do_testu = [
            "100",
            "single",
            "200",
            "1",
            "Jan",
            "Kowalski",
            "jankowalski@email.com",
            "123456789"
        ]

        mock_input.side_effect = dane_do_testu
        add_room()
        register_guest()

        gosc_id = list(guest_reservations.keys())[0]


        mock_input.side_effect = [gosc_id, dzisiaj.strftime("%Y-%m-%d"),
                                  jutro.strftime("%Y-%m-%d"), "100", "karta"]
        make_reservation()

        platnosc = list(payments.values())[0]
        mock_input.side_effect = [platnosc.payment_id]
        confirm_payment()

        mock_input.side_effect = [gosc_id, dzisiaj.strftime("%Y-%m-%d")]
        check_guest_room()


        mock_input.side_effect = ["100"]
        show_room_reservations()

        mock_input.side_effect = [gosc_id]
        show_guest_payments()

        export_reservations_to_csv()
        self.assertTrue(os.path.exists("rezerwacje_export.csv"))
        print("Plik CSV został wygenerowany.")

        mock_input.side_effect = [
            dzisiaj.strftime("%Y-%m-%d"),
            jutro.strftime("%Y-%m-%d")
        ]
        show_available_rooms()

if __name__ == '__main__':
    unittest.main()