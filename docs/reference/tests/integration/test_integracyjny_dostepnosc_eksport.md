# Test `TestIntegracyjnyDostepnoscEksport`

Test integracyjny sprawdzający pełny przebieg procesu rezerwacyjnego:  
od dodania pokoju i rejestracji gościa, przez dokonanie i opłacenie rezerwacji,  
aż po sprawdzenie historii płatności, dostępności pokoi i eksport danych do pliku CSV.

Weryfikowane są następujące funkcjonalności:
- dodanie pokoju do hotelu,
- rejestracja gościa,
- dokonanie i opłacenie rezerwacji,
- przypisanie gościa do pokoju w danym terminie,
- sprawdzenie historii rezerwacji i płatności,
- eksport danych do pliku `.csv`,
- filtrowanie dostępnych pokoi.

---

## Dokumentacja techniczna

::: tests.integration.test_integracyjny_dostepnosc_eksport.TestIntegracyjnyDostepnoscEksport
