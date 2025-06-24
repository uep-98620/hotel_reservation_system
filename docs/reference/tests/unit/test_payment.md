# Test `TestPayment`

Test jednostkowy dla klasy `Payment`, sprawdzający poprawność tworzenia płatności oraz działania jej metod.

Zakres testów obejmuje:
- tworzenie płatności z różnymi metodami (karta/gotówka),
- walidację poprawności danych wejściowych (rezerwacja, metoda płatności),
- potwierdzanie płatności i aktualizację jej statusu,
- obsługę ponownego potwierdzania tej samej płatności,
- metody informacyjne: `is_paid()`, `get_summary()`, `__str__()` i `__repr__()`,
- obsługę różnych kwot wynikających z rezerwacji (liczba nocy × cena pokoju).

Testy wykonują również weryfikację typu danych oraz wartości zwracanych przez metody klasy.

---

## Dokumentacja techniczna

::: tests.unit.test_payment.TestPayment
