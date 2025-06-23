# Klasa `Reservation`

Klasa `Reservation` reprezentuje pojedynczą rezerwację dokonaną przez gościa w systemie hotelowym.

Zawiera informacje o dacie zameldowania, wymeldowania, wybranym pokoju oraz osobie dokonującej rezerwacji.  

Pozwala obliczyć łączny koszt pobytu, liczbę nocy oraz wygenerować podsumowanie rezerwacji.

---

## Dokumentacja techniczna

::: models.reservation.Reservation

---

## Przykład użycia

```python
from models.reservation import Reservation
from models.guest import Guest
from models.room import Room
from datetime import date

guest = Guest("Anna", "Nowak", "anna.nowak@email.com", "123456789")
room = Room("101", "double", 200.0, 2)
check_in = date(2025, 7, 23)
check_out = date(2025, 7, 26)

rezerwacja = Reservation(guest, room, check_in, check_out)

print(rezerwacja.get_duration())
print(rezerwacja.get_total_price())
print(rezerwacja.get_summary())
```