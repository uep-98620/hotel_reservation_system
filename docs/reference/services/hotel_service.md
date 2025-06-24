# Klasa `HotelService`

Klasa `HotelService` stanowi główną logikę aplikacyjną systemu zarządzania hotelem.  
Łączy funkcje związane z pokojami, gośćmi, rezerwacjami i płatnościami, zapewniając wygodny interfejs do operacji biznesowych.

Umożliwia m.in. dodawanie pokoi, rejestrację gości, tworzenie rezerwacji, przetwarzanie płatności oraz sprawdzanie dostępności.

---

## Dokumentacja techniczna

::: services.hotel_service.HotelService

---

## Przykład użycia

```python
from services.hotel_service import HotelService
from datetime import date

# Tworzenie hotelu
service = HotelService("Hotel Warszawa", "ul. Przykładowa 1")

# Dodanie pokoju
room = service.add_room("101", "double", 300.0, 2)

# Rejestracja gościa
guest = service.register_guest("Anna", "Kowalska", "anna@example.com", "555-123-456")

# Tworzenie rezerwacji
check_in = date(2025, 8, 1)
check_out = date(2025, 8, 5)
reservation = service.make_reservation(guest, "101", check_in, check_out)

# Płatność
payment = service.create_payment(reservation, "przelew")
service.confirm_payment(payment)
```