import uuid
from typing import Dict, Any

class Guest:
    """Reprezentuje gościa hotelu.

    Atrybuty:
        guest_id (str): Unikatowy identyfikator gościa hotelu.
        first_name (str): Imię gościa.
        last_name (str): Nazwisko gościa.
        email (str): Adres e-mail gościa.
        phone_number (str): Numer telefonu gościa.
    """
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        """Inicjalizuje obiekt Guest z unikalnym ID."""
        if not first_name or not isinstance(first_name, str):
            raise ValueError("Imię nie może być puste.")
        if not last_name or not isinstance(last_name, str):
             raise ValueError("Nazwisko nie może być puste.")
        if not email or "@" not in email or "." not in email.split("@")[1]:
             raise ValueError("Nieprawidłowy format adresu e-mail.")
        if not phone_number or not isinstance(phone_number, str):
             raise ValueError("Numer telefonu nie może być pusty.")


        self.guest_id: str = str(uuid.uuid4())
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.phone_number: str = phone_number

    def get_full_name(self) -> str:
        """Zwraca pełne imię gościa.

        Zwraca:
            str: Imię i nazwisko.
        """
        return f"{self.first_name} {self.last_name}"

    def get_contact_info(self) -> Dict[str, str]:
        """Zwraca informacje kontaktowe gościa.

        Zwraca:
            Dict[str, str]: Słownik z adresem e-mail i numerem telefonu.
        """
        return {"email": self.email, "phone_number": self.phone_number}

    def __str__(self) -> str:
        return f"Gość: {self.get_full_name()} (ID: {self.guest_id})"

    def __repr__(self) -> str:
        return (f"Gość(ID='{self.guest_id}', imię='{self.first_name}', "
                f"nazwisko='{self.last_name}', email='{self.email}', "
                f"numer telefonu='{self.phone_number}')")