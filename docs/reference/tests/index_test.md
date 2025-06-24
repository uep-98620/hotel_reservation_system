# Przegląd testów

W projekcie zastosowano zarówno testy jednostkowe, jak i integracyjne w celu zapewnienia poprawności działania aplikacji.

Testy zostały podzielone na dwa główne typy:

- **Testy jednostkowe** — sprawdzają poprawność działania pojedynczych klas, ich metod oraz walidację danych wejściowych.
- **Testy integracyjne** — weryfikują pełne scenariusze użycia programu: od rejestracji gościa, przez tworzenie rezerwacji i obsługę płatności, aż po eksport danych.

---

## Testy jednostkowe (pojedyncze klasy)

- [Guest](unit/Test_guest_class.md) — testy poprawności danych gościa oraz metod informacyjnych
- [Room](unit/test_room.md) — testy poprawności pokoju, walidacji oraz reprezentacji tekstowej
- [Hotel](unit/test_hotel.md) — testy zarządzania pokojami i rezerwacjami
- [Payment](unit/test_payment.md) — testy metod płatności, statusów oraz podsumowań
- [Reservation](unit/test_reservation.md) — testy rezerwacji, zakresu dat oraz obliczeń

---

## Testy integracyjne (działanie programu)

- [Rezerwacja i płatność](integration/test_integracyjny_rezerwacja_platnosc.md) — pełny przebieg od dodania pokoju do potwierdzenia płatności
- [Anulowanie i zwrot](integration/test_integracyjny_anulowanie_zwrot.md) — scenariusz anulowania rezerwacji i zwrotu środków
- [Dostępność i eksport](integration/test_integracyjny_dostepnosc_eksport.md) — test filtrowania dostępnych pokoi oraz eksportu danych do pliku
