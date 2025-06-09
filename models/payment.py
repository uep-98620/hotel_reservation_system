import uuid
from typing import Literal
from models.reservation import Reservation

class Payment:
    """
    Reprezentuje płatność za konkretną rezerwację.
    """

    def __init__(self, reservation: Reservation, method: Literal["karta", "gotówka"]):
        """
        Tworzy obiekt płatności.

        :param reservation: Rezerwacja, za którą ma być wykonana płatność.
        :param method: Metoda płatności – 'karta' albo 'gotówka'.
        """

        if not isinstance(reservation, Reservation):
            raise TypeError("Musisz podać poprawną rezerwację.")

        if method not in ["karta", "gotówka"]:
            raise ValueError("Metoda płatności musi być 'karta' albo 'gotówka'.")

        self.payment_id: str = str(uuid.uuid4())
        self.reservation: Reservation = reservation
        self.method: str = method
        self.amount: float = reservation.get_total_price()
        self.paid: bool = False

    def confirm_payment(self) -> None:
        """
        Zaznacza, że płatność została wykonana.
        """
        self.paid = True

    def is_paid(self) -> bool:
        """
        Zwraca True, jeśli płatność została potwierdzona.
        """
        return self.paid