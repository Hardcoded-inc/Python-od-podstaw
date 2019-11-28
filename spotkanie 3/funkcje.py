# Funkcje
def wypisz_tekst():  # Funkcja wypisująca
    """Dokumentacja funkcji (Wypisywanie tekstu)"""
    print("Jestem funkcją, wypisuje tekst \n")


def przyjmuje_i_zwracam(x, y):  # Funkcja przyjmująca argumenty i zwracająca
    """Sumowanie 2 liczb"""
    z = x + y
    return z


def przyjmuje_i_zwracam_mam_wartości_domyslne(x=1, y=2):  # Funkcja przyjmująca argumenty i zwracająca z wartościami domyślnymi
    """Sumowanie 2 liczb, funkcja ma wartości domyślne"""
    z = x + y
    return z


def daj_mi_5():  # Funkcja zwracająca
    """Zwraca 5"""
    liczba = 5
    return liczba


wypisz_tekst()
print(przyjmuje_i_zwracam(7, 10))
print(przyjmuje_i_zwracam_mam_wartości_domyslne())
print(daj_mi_5())
