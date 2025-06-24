# Test `ReservationTest`

Test jednostkowy dla klasy `Reservation`, weryfikujący poprawność działania logiki rezerwacyjnej.

Zakres testów obejmuje:
- poprawne tworzenie rezerwacji na podstawie gościa, pokoju i zakresu dat,
- obliczanie liczby nocy (`get_duration`) i kosztu pobytu (`get_total_price`),
- poprawność danych zwracanych przez metodę `get_summary`,
- walidację typów danych (gość, pokój, daty),
- obsługę nieprawidłowego zakresu dat (check-out przed check-in),
- poprawność reprezentacji tekstowej (`__str__`, `__repr__`).

Testy zapewniają pełne pokrycie funkcjonalności klasy, w tym przypadków błędnych danych wejściowych.

---

## Dokumentacja techniczna

::: tests.unit.test_reservation.ReservationTest
