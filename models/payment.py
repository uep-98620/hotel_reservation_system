class Payment:
    """
    Reprezentuje płatność za konkretną rezerwację.

    Attributes:
        payment_id (str): Unikalny identyfikator płatności.
        reservation (Reservation): Obiekt rezerwacji, do której przypisana jest płatność.
        method (str): Metoda płatności – 'karta' lub 'gotówka'.
        amount (float): Kwota do zapłaty, obliczona na podstawie rezerwacji.
        paid (bool): Status płatności – True jeśli zapłacono, False w przeciwnym razie.
    """

    def __init__(self, reservation: Reservation, method: Literal["karta", "gotówka"]):
        """
        Inicjalizuje obiekt Payment z podaną rezerwacją i metodą płatności.

        Args:
            reservation (Reservation): Rezerwacja, za którą ma być wykonana płatność.
            method (Literal["karta", "gotówka"]): Metoda płatności.

        Raises:
            TypeError: Jeśli reservation nie jest obiektem klasy Reservation.
            ValueError: Jeśli metoda płatności nie jest 'karta' ani 'gotówka'.
        """
        ...

    def confirm_payment(self) -> None:
        """
        Oznacza płatność jako zakończoną (paid = True).
        """

    def is_paid(self) -> bool:
        """
        Sprawdza, czy płatność została już zrealizowana.

        Returns:
            bool: True jeśli płatność została potwierdzona, False w przeciwnym razie.
        """