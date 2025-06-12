# Hotel Reservation System

Projekt zespołowy w Pythonie.

##  Cel projektu

Stworzenie systemu rezerwacji pokojów hotelowych z wykorzystaniem:
- klas Pythona z typowaniem i dokumentacją
- testów jednostkowych i integracyjnych
- współpracy zespołowej na GitHubie (branże, PR, review)
- czytelnej struktury projektu

---

##  Struktura katalogów

```plaintext
main.py
models/
services/
utils/
tests/
├── unit/
└── integration/

## Zespół projektowy i podział obowiązków

Projekt został zrealizowany zespołowo w ramach współpracy pięciu osób.

| Imię       | Obszary odpowiedzialności                                                                 |
|------------|--------------------------------------------------------------------------------------------|
| **Ola**    | - Inicjalizacja repozytorium i dodanie członków<br> - Struktura projektu<br> - Branch `feature_payment`<br> - Testowanie: `feature_payment`, `hotel_class`, `guest_class`<br> - Merge: `reservation_class` do `DEV`<br> - Implementacja logiki<br> - Szkielet pliku README.md<br> - MERGE do `main` z tagiem `v1.0`<br> - Test końcowy |
| **Weronika** | - Branch `guest_class` (kod gotowy na repo Patryka)<br> - Testowanie: `guest_class`, `implement_room_class`, `feature_payment`<br> - Merge: `hotel_class` do `DEV`<br> - Test integracyjny 1<br> - Opis branchy i wymaganych bibliotek<br> - Docstringi klas |
| **Patryk** | - Branch `hotel_class` (kod gotowy na repo Patryka)<br> - Testowanie: `hotel_class`, `implement_room_class`, `reservation_class`<br> - Merge: `implement_room_class` do `DEV` |
| **Czarek** | - Branch `implement_room_class` (kod gotowy na repo Patryka)<br> - Testowanie: `implement_room_class`, `reservation_class`, `guest_class`<br> - Merge: `guest_class` do `DEV`<br> - Test integracyjny 2<br> - Skład zespołu + opis obowiązków (README)<br> - Sprawdzenie typowania funkcji i klas |
| **Martyna**| - Branch `reservation_class` (kod gotowy na repo Patryka)<br> - Testowanie: `reservation_class`, `feature_payment`, `hotel_class`<br> - Merge: `feature_payment` do `DEV`<br> - Test integracyjny 3<br> - Instrukcja działania + przykłady użycia (README)<br> - Plik `requirements.txt` |

Każdy członek zespołu aktywnie uczestniczył w pracach programistycznych, testowaniu i finalnym przygotowaniu projektu do wersji produkcyjnej.
