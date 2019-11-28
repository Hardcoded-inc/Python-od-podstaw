# Slowniki

# tworzenie słownika
slownik = {
    "klucz": "wyjaśnienie hasła",
    "python": "Zajebisty język programowania"
}

# wyświetlanie zawartości słownika
print(slownik["python"])

print(slownik.get("python2", "Klucz nie istenieje"))

# dopisywanie wartości do słownika

slownik["c++"] = "Coś czego musimy się uczyć"

# metody słownika

print(slownik.keys())
print(slownik.values())
print(slownik.items())

