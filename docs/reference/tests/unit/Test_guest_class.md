# Test `GuestTest`

Test jednostkowy dla klasy `Guest`, weryfikujący poprawność tworzenia obiektów oraz działania metod publicznych klasy.

Sprawdzane są następujące aspekty:
- poprawna inicjalizacja danych gościa (imię, nazwisko, e-mail, numer telefonu),
- unikalność identyfikatora gościa (`guest_id`),
- działanie metod `get_full_name()` oraz `get_contact_info()`,
- reprezentacje tekstowe: `__str__()` i `__repr__()`,
- obsługa błędów przy nieprawidłowych danych wejściowych (brak imienia/nazwiska, błędny e-mail, numer telefonu w złym formacie lub pusty).

---

## Dokumentacja techniczna

::: tests.unit.Test_guest_class.GuestTest
