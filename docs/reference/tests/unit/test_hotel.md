# Test `TestHotel`

Test jednostkowy dla klasy `Hotel`, sprawdzający jej kluczowe funkcjonalności związane z zarządzaniem pokojami i rezerwacjami.

Zakres testów obejmuje:
- dodawanie pokoi i zapobieganie duplikatom,
- filtrowanie pokoi po typie i pojemności,
- wyszukiwanie pokoi po numerze,
- tworzenie rezerwacji w dostępnych terminach,
- obsługę konfliktu terminów rezerwacji,
- weryfikację dostępności pokoju na zadany przedział czasu.

Testy operują na instancji hotelu z dwoma pokojami oraz jednym gościem utworzonym w metodzie `setUp()`.

---

## Dokumentacja techniczna

::: tests.unit.test_hotel.TestHotel
