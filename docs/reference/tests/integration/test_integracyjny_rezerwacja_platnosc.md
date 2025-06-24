# Test `TestIntegracyjnyRezerwacja`

Test integracyjny sprawdzający poprawność procesu rezerwacji oraz płatności.  
Obejmuje pełny przebieg: od dodania pokoju, przez rejestrację gościa, aż po stworzenie rezerwacji i potwierdzenie płatności.

Weryfikowane są:
- poprawne dodanie pokoju do systemu,
- rejestracja gościa i zapisanie jego danych,
- przypisanie rezerwacji do gościa i pokoju w określonym terminie,
- utworzenie obiektu płatności oraz zmiana jej statusu po potwierdzeniu.

---

## Dokumentacja techniczna

::: tests.integration.test_integracyjny_rezerwacja_platnosc.TestIntegracyjnyRezerwacja
