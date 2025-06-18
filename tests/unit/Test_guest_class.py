import unittest
from guest import Guest

class GuestTest(unittest.TestCase):
    """ Test dla klasy Guest - weryfikuje poprawność tworzenia danych o gościu oraz działania metod klasy.  """
    def test_create_guest(self):
        """ Test poprawności utworzenia obiektu gościa składającego się z takich danych jak:
         imię, nazwisko, adres e-mail, numer telefonu. Weryfikacja poprawności zapisania danych oraz nadania unikalnego ID. """
        guest = Guest("Jan", "Kowalski", "jankowalski@email.com", "91123456789")
        self.assertIsInstance(guest.guest_id, str)
        self.assertEqual(guest.first_name, "Jan")
        self.assertEqual(guest.last_name, "Kowalski")
        self.assertEqual(guest.email, "jankowalski@email.com")
        self.assertEqual(guest.phone_number, "91123456789")

    def test_get_full_name(self):
        """ Test działania metody get_full_name - czy zwraca pełne imię i nazwisko gościa."""
        guest = Guest("Adam", "Nowak", "adamnowak@email.com", "123456789")
        self.assertEqual(guest.get_full_name(), "Adam Nowak")

    def test_get_contact_info(self):
        """ Test działania metody get_contact_info - czy zwraca dane dotyczące adresu e-mail oraz numeru telefonu gościa
        w formie słownika."""
        guest= Guest("Anna", "Kowalska", "annakowalska@email.com", "543871091")
        contact = guest.get_contact_info()
        self.assertEqual(contact["email"], "annakowalska@email.com")
        self.assertEqual(contact["phone_number"], "543871091")

    def test_str_representation(self):
        """ Weryfikacja czy po wyświetleniu gościa widać jego imię i nazwisko. """
        guest = Guest("Kazimierz", "Nowakowski", "kazimierz@email.com", "443809091")
        self.assertIn("Gość: Kazimierz Nowakowski", str(guest))

    def test_repr(self):
        """ Weryfikacja czy techniczny opis obiektu zawiera pożądane informacje o gościu hotelu."""
        guest = Guest("Joanna", "Niewiadomska", "joanna@email.com", "777871091")
        rep = repr(guest)
        self.assertIn("Gość(ID=", rep)
        self.assertIn("imię='Joanna'", rep)
        self.assertIn("nazwisko='Niewiadomska'", rep)

    def test_empty_first_name(self):
        """ Weryfikacja czy program zwróci błąd ValueError, gdy nie zostanie podane imię gościa."""
        with self.assertRaises(ValueError):
            Guest("", "Nowakowski", "kazimierz@email.com", "443809091")

    def test_empty_last_name(self):
        """ Weryfikacja czy program zwróci błąd ValueError, gdy nie zostanie podane nazwisko gościa."""
        with self.assertRaises(ValueError):
            Guest("Adam", "", "adamnowak@email.com", "123456789")

    def test_invalid_email(self):
        """ Weryfikacja czy program zwróci błąd ValueError, gdy podany adres e-mail nie posiada poprawnego formatu adresu
        mailowego. """
        with self.assertRaises(ValueError):
            Guest("Anna", "Kowalska", "nomail", "543871091")

    def test_empty_phone_number(self):
        """Weryfikacja czy program zwróci błąd ValueError, gdy nie zostanie podany numer telefonu."""
        with self.assertRaises(ValueError):
            Guest("Joanna", "Niewiadomska", "joanna@email.com", "")

    def test_phone_number_not_string(self):
        """Weryfikacja czy program zwróci błąd ValueError, gdy numer telefonu nie zostanie podany w formie tekstowej (string)."""
        with self.assertRaises(ValueError):
            Guest("Jan", "Kowalski", "jankowalski@email.com", 123456789)

    if __name__ == "__main__":
        unittest.main()