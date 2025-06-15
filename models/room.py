from typing import Dict, Any

class Room:
    """Reprezentuje pokój hotelowy.

    Atrybuty:
        number (str): Numer pokoju.
        room_type (str): Typ pokoju (np. single, double, suite).
        price_per_night (float): Cena za jedną noc.
        capacity (int): Maksymalna liczba gości w pokoju.
    """
    def __init__(self, number: str, room_type: str, price_per_night: float, capacity: int):
        """Inicjalizuje obiekt Room."""
        if not number or not isinstance(number, str):
            raise ValueError("Numer pokoju nie może być pusty.")
        if not room_type or not isinstance(room_type, str):
            raise ValueError("Typ pokoju nie może być pusty.")
        if not isinstance(price_per_night, (int, float)) or price_per_night <= 0:
            raise ValueError("Cena za noc musi być liczbą dodatnią.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Pojemność pokoju musi być liczbą całkowitą większą od zera.")

        self.number: str = number
        self.room_type: str = room_type
        self.price_per_night: float = float(price_per_night)
        self.capacity: int = capacity

    def get_details(self) -> Dict[str, Any]:
        """Zwraca szczegóły pokoju.

        Zwraca:
            Dict[str, Any]: Słownik z numerem, typem, ceną i pojemnością pokoju.
        """
        return {
            "numer": self.number,
            "typ_pokoju": self.room_type,
            "cena_za_noc": self.price_per_night,
            "pojemnosc": self.capacity,
        }

    def __str__(self) -> str:
        return f"Pokój: {self.number} ({self.room_type}), {self.capacity} os., {self.price_per_night:.2f} zł/noc"

    def __repr__(self) -> str:
        return (f"Pokój(numer='{self.number}', typ_pokoju='{self.room_type}', "
                f"cena_za_noc={self.price_per_night}, pojemnosc={self.capacity})")
if __name__ == "__main__":
    room = Room("101", "single", 150.0, 2)
    print(room)
    print(room.get_details())
    print(repr(room))