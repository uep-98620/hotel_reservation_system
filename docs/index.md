# System Rezerwacji Hotelowej

Witamy w dokumentacji systemu rezerwacji hotelowej — projektu stworzonego w ramach zajęć z inżynierii oprogramowania.

System umożliwia zarządzanie pokojami hotelowymi, gośćmi, rezerwacjami oraz płatnościami poprzez prosty interfejs tekstowy (CLI). 

Dokumentacja zawiera opisy struktury projektu, klas danych, logiki działania oraz zestaw testów potwierdzających poprawność działania aplikacji.

---

## Struktura dokumentacji

- [Klasy danych](reference/index_klasy.md)  
  Opis klas: `Guest`, `Room`, `Reservation`, `Hotel` i `Payment`

- [Logika aplikacyjna](reference/services/hotel_service.md)  
  Sposób działania systemu oraz powiązania między komponentami

- [Interfejs użytkownika (CLI)](reference/main.md)  
  Przegląd dostępnych komend i interakcji z systemem

- [Testy](reference/tests/index_test.md)  
  Testy jednostkowe i integracyjne weryfikujące poprawność działania

---

## Uruchomienie projektu

1. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

2. Uruchom aplikację:
   ```bash
   python main.py
   ```

3. Otwórz dokumentację lokalnie:
   ```bash
   mkdocs serve
   ```

---

## Technologie użyte w projekcie

- Python 3.12
- MkDocs + Material for MkDocs
- `unittest` – testowanie jednostkowe i integracyjne
- `mkdocstrings` – automatyczna dokumentacja kodu

---

_Dokumentacja opracowana przez grupę tworzącą projekt.
