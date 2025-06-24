# Klasa `Room`

Klasa `Room` reprezentuje pokój hotelowy dostępny do rezerwacji.

Zawiera dane dotyczące numeru pokoju, jego typu (np. single, double), ceny za noc oraz maksymalnej liczby gości.  
Może być wykorzystywana przy tworzeniu rezerwacji i filtrowaniu dostępnych opcji noclegu.

---

## Dokumentacja techniczna

::: models.room.Room

---

## Przykład użycia

```python
from models.room import Room

pokoj = Room("101", "double", 200.0, 2)

print(pokoj.number)      
print(pokoj.room_type)   
print(pokoj.price_per_night)
print(pokoj.capacity)
```