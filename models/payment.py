import uuid
from typing import Literal, Optional, Dict, Any
from datetime import datetime
from .reservation import Reservation

class Payment:
    """Reprezentuje płatność za konkretną rezerwację."""

    def __init__(self, reservation: Reservation, method: Literal["karta", "gotówka"]):
        if not isinstance(reservation, Reservation):
            raise TypeError("Rezerwacja nie znaleziona.")
        if method not in ("karta", "gotówka"):
            raise ValueError("Metoda płatności musi być 'karta' lub 'gotówka'.")

        self.payment_id: str = str(uuid.uuid4())
        self.reservation: Reservation = reservation
        self.method: str = method
        self.amount: float = reservation.get_total_price()
        self.paid: bool = False
        self.payment_date: Optional[datetime] = None

    def confirm_payment(self) -> None:
        """Oznacza płatność jako zakończoną."""
        if self.paid:
            raise ValueError("Płatność została już wcześniej potwierdzona.")
        self.paid = True
        self.payment_date = datetime.now()

    def is_paid(self) -> bool:
        """Sprawdza, czy płatność została już zrealizowana."""
        return self.paid

    def get_summary(self) -> Dict[str, Any]:
        """Zwraca podsumowanie płatności."""
        return {
            "payment_id": self.payment_id,
            "reservation_id": self.reservation.reservation_id,
            "guest_name": self.reservation.guest.get_full_name(),
            "amount": self.amount,
            "method": self.method,
            "paid": self.paid,
            "payment_date": self.payment_date.isoformat() if self.payment_date else None
        }

    def __str__(self) -> str:
        status = "opłacona" if self.paid else "oczekuje na płatność"
        return f"Płatność {self.payment_id} ({self.method}) – {status}"

    def __repr__(self) -> str:
        return (f"Płatność(payment_id='{self.payment_id}', amount={self.amount}, "
                f"method='{self.method}', paid={self.paid}, "
                f"payment_date={self.payment_date})")
