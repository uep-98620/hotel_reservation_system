# Główna aplikacja (CLI)

Moduł `main.py` pełni rolę interfejsu tekstowego (CLI) umożliwiającego użytkownikowi interakcję z systemem rezerwacji hotelowej.  

Pozwala na dodawanie pokoi, rejestrację gości, dokonywanie rezerwacji, opłacanie, anulowanie i przeglądanie rezerwacji, a także eksport danych.

Ten moduł łączy wszystkie komponenty aplikacji: modele, logikę i dane, umożliwiając ich użycie w praktyce.

---

## Dostępne funkcje CLI

System oferuje następujące opcje:

1. **Dodaj pokój** – umożliwia dodanie nowego pokoju do hotelu  
2. **Zarejestruj gościa** – dodaje nowego gościa do bazy  
3. **Utwórz rezerwację** – pozwala na zarezerwowanie pokoju  
4. **Zobacz dostępność pokoi** – sprawdza, które pokoje są wolne  
5. **Wyświetl rezerwacje** – pokazuje wszystkie rezerwacje  
6. **Anuluj rezerwację** – umożliwia anulowanie istniejącej rezerwacji  
7. **Potwierdź płatność** – oznacza rezerwację jako opłaconą  
8. **Zwrot płatności** – pozwala zwrócić środki za rezerwację  
9. **Sprawdź pokój gościa** – pokazuje, w którym pokoju przebywa gość  
10. **Historia rezerwacji pokoju** – przegląd rezerwacji danego pokoju  
11. **Historia płatności gościa** – lista wszystkich płatności danego gościa  
12. **Eksport rezerwacji do CSV** – generuje plik CSV z rezerwacjami

Użytkownik wybiera opcje za pomocą klawiatury, a dane są podawane interaktywnie przez `input()`.

---

## Dokumentacja techniczna

::: main

---

## Przykład uruchomienia

```bash
python main.py
```


