# Klasa `Payment`

Klasa `Payment` reprezentuje płatność powiązaną z rezerwacją w systemie hotelowym.  
Obsługuje informacje o metodzie płatności, statusie, kwocie oraz dacie jej realizacji.

Dzięki tej klasie można potwierdzić płatność, sprawdzić czy została zrealizowana oraz uzyskać podsumowanie.

---

## Dokumentacja techniczna

::: models.payment.Payment

---

## Przykład użycia

```python
from models.payment import Payment
from models.reservation import Reservation
from models.guest import Guest
from models.room import Room
from datetime import date

guest = Guest("Jan", "Kowalski", "jan@example.com", "123456789")
room = Room("101", "single", 150.0, 1)
reservation = Reservation(guest, room, date(2025, 7, 10), date(2025, 7, 12))

payment = Payment(reservation, method="karta")
print(payment.is_paid())
payment.confirm_payment()
print(payment.get_summary())
```
