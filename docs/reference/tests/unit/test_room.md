# Test `TestRoom`

Test jednostkowy dla klasy `Room`, sprawdzający poprawność tworzenia obiektu pokoju oraz walidację jego atrybutów.

Zakres testów obejmuje:
- prawidłową inicjalizację pokoju z numerem, typem, ceną i pojemnością,
- obsługę błędów przy niepoprawnych danych wejściowych (pusty numer, błędna cena, pojemność jako tekst itd.),
- działanie metody `get_details()` – zwracającej słownik z informacjami o pokoju,
- poprawność reprezentacji tekstowej metod `__str__()` i `__repr__()`.

Testy zapewniają kompletne pokrycie scenariuszy dla klasy `Room`, w tym przypadków brzegowych i niepoprawnych danych.

---

## Dokumentacja techniczna

::: tests.unit.test_room.TestRoom
