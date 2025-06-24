from datetime import date, datetime
from models.guest import Guest
from models.room import Room
from models.hotel import Hotel
from models.reservation import Reservation
from models.payment import Payment
import csv

hotel = Hotel("Hotel CLI", "ul. Terminalowa 42, Konsolowo")
guests = {}
payments = {}
guest_reservations = {}  # guest_id -> list of Reservation
cancelled_reservations = set()
refunded_payments = set()

def get_date(prompt):
    """
    Prosi użytkownika o datę w formacie RRRR-MM-DD.

    Args:
        prompt (str): Komunikat wyświetlany użytkownikowi.

    Returns:
        date: Obiekt daty (datetime.date).
    """
    while True:
        try:
            return datetime.strptime(input(prompt), "%Y-%m-%d").date()
        except ValueError:
            print("Błąd: nieprawidłowy format. Podaj datę w formacie RRRR-MM-DD.")

def add_room():
    """
    Interaktywne dodanie nowego pokoju do hotelu.
    Pobiera dane od użytkownika i tworzy instancję Room.
    """
    print("\nDodawanie pokoju")
    number = input("Numer pokoju: ")
    room_type = input("Typ pokoju (np. single, double): ")
    try:
        price = float(input("Cena za noc: "))
        capacity = int(input("Pojemność: "))
        room = Room(number, room_type, price, capacity)
        hotel.add_room(room)
        print("Pokój dodany.\n")
    except Exception as e:
        print(f"Błąd: {e}\n")

def register_guest():
    """
    Rejestruje nowego gościa hotelowego.
    Tworzy instancję Guest i zapisuje ją do słownika `guests`.
    """
    print("\nRejestracja gościa")
    first = input("Imię: ")
    last = input("Nazwisko: ")
    email = input("Email: ")
    phone = input("Telefon: ")
    try:
        guest = Guest(first, last, email, phone)
        guests[guest.guest_id] = guest
        guest_reservations[guest.guest_id] = []
        print(f"Gość zarejestrowany. ID: {guest.guest_id}\n")
    except Exception as e:
        print(f"Błąd: {e}\n")

def show_available_rooms():
    """
    Wyświetla dostępne pokoje w zadanym przedziale dat.
    Pobiera daty od użytkownika i przeszukuje listę pokoi.
    """
    print("\nDostępność pokoi")
    check_in = get_date("Data zameldowania (YYYY-MM-DD): ")
    check_out = get_date("Data wymeldowania (YYYY-MM-DD): ")

    print("Dostępne pokoje:")
    available = []

    for room in hotel.get_all_rooms():
        if hotel.is_room_available(room, check_in, check_out):
            available.append(room)
            print(room)

    if not available:
        print("Brak dostępnych pokoi w tym terminie.\n")
    else:
        print()

def make_reservation():
    """
    Tworzy nową rezerwację dla zarejestrowanego gościa.
    Sprawdza dostępność pokoi, zapisuje rezerwację i inicjuje płatność.
    """
    print("\nTworzenie rezerwacji")
    guest_id = input("Podaj ID gościa: ")
    guest = guests.get(guest_id)
    if not guest:
        print("Nie znaleziono gościa.\n")
        return

    check_in = get_date("Data zameldowania (YYYY-MM-DD): ")
    check_out = get_date("Data wymeldowania (YYYY-MM-DD): ")

    print("Dostępne pokoje:")
    available_rooms = []
    for room in hotel.get_all_rooms():
        if hotel.is_room_available(room, check_in, check_out):
            available_rooms.append(room)
            print(room)

    if not available_rooms:
        print("Brak dostępnych pokoi w tym terminie.\n")
        return

    room_number = input("Numer pokoju do rezerwacji: ")
    room = hotel.find_room_by_number(room_number)
    if not room or not hotel.is_room_available(room, check_in, check_out):
        print("Pokój niedostępny.\n")
        return

    try:
        reservation = hotel.make_reservation(guest, room_number, check_in, check_out)
        guest_reservations[guest.guest_id].append(reservation)
        print("Rezerwacja utworzona.")
        for key, value in reservation.get_summary().items():
            print(f"{key}: {value}")

        method = input("Metoda płatności (karta/gotówka): ").strip().lower()
        payment = Payment(reservation, method)
        payments[payment.payment_id] = payment
        print(f"Płatność utworzona. ID: {payment.payment_id}\n")

    except Exception as e:
        print(f"Błąd: {e}\n")

def list_reservations():
    """
    Wyświetla wszystkie rezerwacje w systemie wraz ze statusem (aktywna/anulowana).
    """
    print("\nLista rezerwacji:")
    for res in hotel.get_all_reservations():
        status = "Anulowana" if res.reservation_id in cancelled_reservations else "Aktywna"
        print(f"Rezerwacja {res.reservation_id} - {res.guest.get_full_name()} - Pokój {res.room.number} - Status: {status}")
    print()

def cancel_reservation():
    """
    Anuluje istniejącą rezerwację na podstawie jej ID.
    Aktualizuje zbiór `cancelled_reservations`.
    """
    print("\nAnulowanie rezerwacji")
    res_id = input("Podaj ID rezerwacji: ")
    found = False
    for res in hotel.get_all_reservations():
        if res.reservation_id == res_id:
            cancelled_reservations.add(res_id)
            print("Rezerwacja anulowana.\n")
            found = True
            break
    if not found:
        print("Nie znaleziono rezerwacji.\n")

def confirm_payment():
    """
    Potwierdza płatność za rezerwację na podstawie ID płatności.
    """
    print("\nPotwierdzenie płatności")
    payment_id = input("Podaj ID płatności: ")
    payment = payments.get(payment_id)
    if not payment:
        print("Nie znaleziono płatności.\n")
        return

    try:
        payment.confirm_payment()
        print("Płatność potwierdzona.")
        print(payment)
    except Exception as e:
        print(f"Błąd: {e}\n")

def refund_payment():
    """
    Zarejestrowanie zwrotu płatności.
    Weryfikuje, czy płatność została wcześniej opłacona i nie została już zwrócona.
    """
    print("\nZwrot płatności")
    payment_id = input("Podaj ID płatności: ")
    payment = payments.get(payment_id)
    if not payment or not payment.is_paid():
        print("Nie znaleziono opłaconej płatności.\n")
        return
    if payment_id in refunded_payments:
        print("Ta płatność została już zwrócona.\n")
        return

    refunded_payments.add(payment_id)
    print("Zwrot został zarejestrowany.\n")

def check_guest_room():
    """
    Sprawdza, w jakim pokoju przebywa gość w podanym dniu.
    Weryfikuje aktywne rezerwacje gościa.
    """
    print("\nSprawdzenie pokoju gościa")
    guest_id = input("Podaj ID gościa: ")
    date_to_check = get_date("Data (YYYY-MM-DD): ")
    reservations = guest_reservations.get(guest_id, [])
    for res in reservations:
        if res.reservation_id not in cancelled_reservations and res.check_in <= date_to_check < res.check_out:
            print(f"Gość przebywa w pokoju {res.room.number}.")
            return
    print("Gość nie ma aktywnej rezerwacji w tym dniu.\n")

def show_room_reservations():
    """
    Wyświetla historię wszystkich rezerwacji danego pokoju.
    Wypisuje szczegóły każdej rezerwacji.
    """
    print("Historia rezerwacji pokoju")
    room_number = input("Podaj numer pokoju: ")
    found = False
    for res in hotel.get_all_reservations():
        if isinstance(res, Reservation) and res.room.number == room_number:
            print("---")
            print(f"ID: {res.reservation_id}")
            print(f"Gość: {res.guest.get_full_name()}")
            print(f"Pokój: {res.room.number}")
            print(f"Zameldowanie: {res.check_in}")
            print(f"Wymeldowanie: {res.check_out}")
            print(f"Liczba nocy: {res.get_duration()}")
            print(f"Cena całkowita: {res.get_total_price()} zł")
            print("Status: Anulowana" if res.reservation_id in cancelled_reservations else "Status: Aktywna")
            print()
            found = True
    if not found:
        print("Brak rezerwacji dla tego pokoju.")

def show_guest_payments():
    """
    Pokazuje historię płatności dla danego gościa.
    Wskazuje status każdej płatności (opłacona/nieopłacona/zwrócona).
    """
    print("\nHistoria płatności gościa")
    guest_id = input("Podaj ID gościa: ")
    for pay in payments.values():
        if pay.reservation.guest.guest_id == guest_id:
            status = "ZWRÓCONA" if pay.payment_id in refunded_payments else ("OPŁACONA" if pay.paid else "NIEOPŁACONA")
            print(f"{pay} - Status: {status}")
    print()

def export_reservations_to_csv():
    """
    Eksportuje wszystkie rezerwacje do pliku CSV o nazwie `rezerwacje_export.csv`.
    Plik zawiera dane gościa, pokoju, daty oraz status.
    """
    filename = "rezerwacje_export.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Gość", "Pokój", "Zameldowanie", "Wymeldowanie", "Noce", "Cena", "Status"])
        for res in hotel.get_all_reservations():
            summary = res.get_summary()
            status = "Anulowana" if res.reservation_id in cancelled_reservations else "Aktywna"
            writer.writerow([
                summary["reservation_id"],
                summary["guest_name"],
                summary["room_number"],
                summary["check_in"],
                summary["check_out"],
                summary["nights"],
                summary["total_price"],
                status
            ])
    print(f"Rezerwacje zapisane do {filename}\n")

def main_menu():
    """
    Główne menu aplikacji hotelowej.
    Obsługuje wybór użytkownika i przekierowuje do odpowiednich funkcji.
    """
    while True:
        print("========= SYSTEM HOTELU =========")
        print("1. Dodaj pokój")
        print("2. Zarejestruj gościa")
        print("3. Utwórz rezerwację")
        print("4. Zobacz dostępność pokoi")
        print("5. Wyświetl rezerwacje")
        print("6. Anuluj rezerwację")
        print("7. Potwierdź płatność")
        print("8. Zwrot płatności")
        print("9. Sprawdź pokój gościa")
        print("10. Historia rezerwacji pokoju")
        print("11. Historia płatności gościa")
        print("12. Eksport rezerwacji do CSV")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            register_guest()
        elif choice == "3":
            make_reservation()
        elif choice == "4":
            show_available_rooms()
        elif choice == "5":
            list_reservations()
        elif choice == "6":
            cancel_reservation()
        elif choice == "7":
            confirm_payment()
        elif choice == "8":
            refund_payment()
        elif choice == "9":
            check_guest_room()
        elif choice == "10":
            show_room_reservations()
        elif choice == "11":
            show_guest_payments()
        elif choice == "12":
            export_reservations_to_csv()
        elif choice == "0":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja.\n")

if __name__ == "__main__":
    main_menu()
