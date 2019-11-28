# Marynowanie, odkładanie na półki

import pickle, shelve  # Import modułów

lista = ["el1", "el2", "el3"]  # Utworzenie listy
file = open("plik_binarny.dat", "wb")  # Otwarcie pliku binarnego w trybie write binary

pickle.dump(lista, file)  # Marynowanie
file.close()  # Zamknięcie pliku binarnego

plik = open("plik_binarny.dat", "rb")  # Otwarcie pliku binarnego w trybie read binary
lista2 = pickle.load(plik)  # Załadowanie pliku binarnego do listy
plik.close()  # Zamknięcie pliku binarnego
print(lista2)

s = shelve.open("pickle.dat")  # Otwarcie półki
s["liczby"] = [1, 2, 3, 4]  # Zapis do indeksu na półce
s["litery"] = ["a", "b", "c"]
s.sync()  # Synchronizacja półki

print("liczby:", s["liczby"])
print("litery:", s["litery"])
s.close()  # Zamykanie półki
