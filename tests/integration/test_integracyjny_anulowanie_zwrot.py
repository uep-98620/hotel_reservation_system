import unittest
from unittest.mock import patch
from datetime import date, timedelta

from main import (hotel, guests, guest_reservations, payments,
                  add_room, register_guest, make_reservation,
                  cancel_reservation, refund_payment, confirm_payment)

class TestIntegracyjnyAnulowanie(unittest.TestCase):
    """Test integracyjny sprawdzający pełny proces: dodanie pokoju, rejestracja gościa,
        dokonanie rezerwacji, opłacenie jej, anulowanie rezerwacji oraz zwrot płatności."""

    @patch('builtins.input')
    def test_anulowanie_i_zwrot(self, mock_input):
        """Test przebiega przez następujące kroki:
        dodanie pokoju do hotelu,
        rejestracja nowego gościa,
        utworzenie rezerwacji dla gościa,
        potwierdzenie płatności,
        anulowanie rezerwacji,
        zwrot środków.

        Każdy etap wykorzystuje symulację danych wejściowych, a po wykonaniu operacji następuje weryfikacja,
        czy system zareagował zgodnie z oczekiwanym przebiegiem logiki biznesowej.
        """

        dzisiaj = date.today()
        jutro = dzisiaj + timedelta(days=1)

        dane_testowe = [
            "100",
            "single",
            "200",
            "1",
            "Jan",
            "Kowalski",
            "jankowalski@email.com",
            "123456789"
        ]

        mock_input.side_effect = dane_testowe
        add_room()
        register_guest()

        gosc_id = list(guests.keys())[0]

        mock_input.side_effect = [
            gosc_id,
            dzisiaj.strftime("%Y-%m-%d"),
            jutro.strftime("%Y-%m-%d"),
            "100",
            "karta"
        ]
        make_reservation()

        platnosc = list(payments.values())[0]
        mock_input.side_effect = [platnosc.payment_id]
        confirm_payment()

        rezerwacja_id = hotel.get_all_reservations()[0].reservation_id
        mock_input.side_effect = [rezerwacja_id]
        cancel_reservation()

        platnosc = list(payments.values())[0]
        mock_input.side_effect = [platnosc.payment_id]
        refund_payment()

if __name__ == '__main__':
    unittest.main()