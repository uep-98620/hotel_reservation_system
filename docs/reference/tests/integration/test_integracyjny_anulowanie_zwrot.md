# Test `TestIntegracyjnyAnulowanie`

Test integracyjny weryfikujący pełen przebieg obsługi rezerwacji w hotelu:
- dodanie pokoju, 
- rejestracja gościa, 
- utworzenie rezerwacji, 
- potwierdzenie płatności, 
- anulowanie rezerwacji,
- zwrot środków.

Test symuluje dane wejściowe za pomocą `unittest.mock.patch` imitując interakcję użytkownika z interfejsem CLI.

---

## Dokumentacja techniczna

::: tests.integration.test_integracyjny_anulowanie_zwrot.TestIntegracyjnyAnulowanie