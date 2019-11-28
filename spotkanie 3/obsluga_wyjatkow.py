# Obsługa wyjątków

try:
    num = float(input("Wprowadź liczbę: "))  # Spróbuj rzutować wpis użytkownika na float
except:
    print("Wystąpił błąd")  # Wypisz w przypadku błędu

try:
    num = float(input("Wprowadź liczbę: "))  # Spróbuj rzutować wpis użytkownika na float
except ValueError:
    print("To nie liczba!")  # Wypisz w przypadku błędu wartości

try:
    num = float(input("Wprowadź liczbę: "))  # Spróbuj rzutować wpis użytkownika na float
except ValueError as e:
    print("To nie liczba, lub w języku pythona", e)  # Wypisz w przypadku błędu wartości i zapisz opis blędu do zmiennej

try:
    num = float(input("Wprowadź liczbę: "))  # Spróbuj rzutować wpis użytkownika na float
except ValueError:
    print("Wystąpił błąd, to nie liczba")  # Wypisz w przypadku błędu wartości
else:
    print("Brak błędów, wprowadzono", num)  # Jeśli nie ma błędów to wykonbaj instrukcje
