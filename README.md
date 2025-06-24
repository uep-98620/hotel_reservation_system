# System Rezerwacji Hotelowej

Projekt zespołowy CLI napisany w języku Python w ramach przedmiotu *Inżynieria Oprogramowania* na kierunku Informatyka i Ekonometria.

System umożliwia kompleksową obsługę rezerwacji pokojów hotelowych — od rejestracji gościa, przez tworzenie i anulowanie rezerwacji, aż po obsługę płatności i eksport danych.

---

## 📑 Dokumentacja

Pełna dokumentacja dostępna pod adresem:  
 [Hotel Reservation System – Dokumentacja](https://uep-98620.github.io/hotel_reservation_system)

---

## 🎯 Cel projektu

Stworzenie systemu rezerwacji pokojów hotelowych z wykorzystaniem:
- klas Pythona z typowaniem i dokumentacją,
- testów jednostkowych i integracyjnych (`unittest`),
- współpracy zespołowej na GitHubie (branche, PR, review),
- interfejsu CLI (Command Line Interface),
- czytelnej dokumentacji z MkDocs.

---

## 📁 Struktura katalogów

```
hotel_reservation_system/
├── main.py
├── models/
├── services/
├── utils/
├── tests/
│   ├── unit/
│   └── integration/
├── docs/
│   ├── index.md
│   └── reference/
└── requirements.txt
```

---

## ⚙️ Technologie

- Python 3.x
- Biblioteki standardowe: `datetime`, `csv`, `typing`, `uuid`
- `unittest` – testowanie
- `mkdocs-material` – dokumentacja projektu
- `mkdocstrings` – automatyczne generowanie opisów klas

---

## 🚀 Instalacja i uruchomienie

1. Klonuj repozytorium:

```bash
git clone https://github.com/uep-98620/hotel_reservation_system.git
cd hotel_reservation_system
```

2. Uruchom aplikację z katalogu głównego projektu:

```bash
python main.py
```

---

## 💻 Przykład działania

Po uruchomieniu aplikacji:

```bash
python main.py
```

Wyświetli się menu:

```
========= SYSTEM HOTELU =========
1. Dodaj pokój
2. Zarejestruj gościa
3. Utwórz rezerwację
4. Zobacz dostępność pokoi
...
13. Wyjście
Wybierz opcję: _
```

---

## 🧪 Testy

Aby uruchomić testy:

```bash
python -m unittest discover tests
```

---

## 👥 Autorzy i podział zadań

| Osoba | Zadania |
|-------|---------|
| **Aleksandra Łuczak** (@uep-98620) | Repozytorium, struktura, logika `main.py`, merge `room.py`, test `guest.py`, test końcowy, README |
| **Weronika Bensch** (@weronikab01) | Klasa `Guest`, merge i test `reservation.py`, test `room.py`, finalne README |
| **Cezary Mikuś** (@czmikus) | Klasa `Hotel`, merge i test `payment.py`, test `reservation.py` |
| **Martyna Borowiec** (@MBorowiec85203) | Klasa `Room`, merge i test `hotel.py`, test `payment.py`, test integracyjny |
| **Patryk Durand** (@patrykd123) | Klasa `Reservation`, merge i test `guest.py`, test `hotel.py`, test integracyjny, `requirements.txt` |

---

**Uwaga:** Projekt zrealizowany w ramach ćwiczeń.
