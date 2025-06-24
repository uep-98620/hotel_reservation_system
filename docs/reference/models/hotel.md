# Klasa `Hotel`

Klasa `Hotel` reprezentuje obiekt hotelowy w systemie rezerwacji.  
Odpowiada za przechowywanie listy pokoi i rezerwacji oraz zarządzanie ich dostępnością i tworzeniem nowych rezerwacji.

Zawiera logikę sprawdzającą dostępność pokoi, filtrowanie po typie i pojemności oraz sprawdza konflikty w rezerwacjach.

---

## Dokumentacja techniczna

::: models.hotel.Hotel

---

## Przykład użycia

```python
from models.hotel import Hotel
from models.room import Room
from models.guest import Guest
from datetime import date

hotel = Hotel("Hotel ChatGPT", "ul. Przykładowa 5")
room = Room("101", "double", 200.0, 2)
hotel.add_room(room)

guest = Guest("Anna", "Nowak", "anna.nowak@email.com", "123456789")
reservation = hotel.make_reservation(guest, "101", date(2025, 7, 1), date(2025, 7, 3))

print(hotel.get_all_rooms())
print(hotel.get_all_reservations())
```
