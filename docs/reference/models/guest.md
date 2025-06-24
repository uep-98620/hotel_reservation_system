# Klasa `Guest`

Klasa `Guest` reprezentuje pojedynczego gościa w systemie rezerwacji hotelowej.

Służy do przechowywania podstawowych danych osobowych i kontaktowych, takich jak imię, nazwisko, e-mail czy numer telefonu.

---

## Dokumentacja techniczna

::: models.guest.Guest

---

## Przykład użycia

```python
from models.guest import Guest

gosc = Guest("Anna", "Nowak", "anna.nowak@email.com", "123456789")
print(gosc.get_full_name())
print(gosc.get_contact_info())
```
