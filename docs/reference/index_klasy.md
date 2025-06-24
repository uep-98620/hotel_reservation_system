# Struktura projektu

Poniżej przedstawiono szczegółowy opis struktury projektu systemu rezerwacji hotelowej. Zawiera on dokumentację klas danych, logiki aplikacyjnej oraz interfejsu użytkownika.

Każdy komponent został opisany w osobnym podrozdziale i zawiera:

- krótki opis funkcji klasy lub modułu,
- automatycznie wygenerowaną dokumentację techniczną metod i atrybutów,
- przykładowy kod użycia w języku Python.

---

## Klasy danych

Reprezentują główne obiekty w systemie: gościa, pokój, rezerwację, płatność i hotel.

- [Guest](models/guest.md) — dane osobowe i kontaktowe gościa
- [Room](models/room.md) — informacje o pokoju hotelowym
- [Reservation](models/reservation.md) — szczegóły dotyczące rezerwacji
- [Hotel](models/hotel.md) — zarządzanie pokojami i rezerwacjami
- [Payment](models/payment.md) — obsługa płatności

---

## Logika aplikacji

Opis głównej logiki biznesowej systemu, łączącej wszystkie komponenty w spójną całość.

- [HotelService](services/hotel_service.md) — zarządza gośćmi, pokojami, rezerwacjami i płatnościami

---

## Interfejs użytkownika (CLI)

Moduł odpowiedzialny za obsługę programu z poziomu wiersza poleceń.

- [main.py](main.md) — interfejs tekstowy umożliwiający użytkownikowi wykonywanie operacji na systemie
