# Pliki tekstowe

# Pliki tekstowe - odczyt

plik_tekstowy = open("plik.txt", "r")  # Otwarcie pliku tekstowego w trybioe odczytu
plik_tekstowy.close()  # Zamknięcie pliku tekstowego

plik_tekstowy = open("plik.txt", "r")
print(plik_tekstowy.read(1))  # Odczytanie pierwszego znaku
plik_tekstowy.close()

plik_tekstowy = open("plik.txt", "r")
caly_tekst = plik_tekstowy.read()  # Odczytanie całego pliku do zmiennej
print(caly_tekst)
plik_tekstowy.close()

plik_tekstowy = open("plik.txt", "r")
print(plik_tekstowy.readline(1))  # Odczytanie 1 znaku z linii
print(plik_tekstowy.readline(3))  # Odczytanie 3 kolejnych znaków z linii
print(plik_tekstowy.readline())  # Odczytanie do końca linii
print(plik_tekstowy.readline())  # Odczytanie całej następnej linii
plik_tekstowy.close()

plik_tekstowy = open("plik.txt", "r")
linie = plik_tekstowy.readlines()  # Odcytanie do listy kadej z linii
print(linie)
for linia in linie:
    print(linia)
plik_tekstowy.close()

# Pliki tekstowe - zapis

plik_zapisu = open("nowy_plik.txt", "w")
plik_zapisu.write("Linia 1 \n")  # Zapisanie tekstu do pliku
plik_zapisu.write("Linia 2 \n")
plik_zapisu.write("Linia 3 \n")
plik_zapisu.close()

lista = ["Wiersz 1 \n", "Wiersz 2\n"]

plik_zapisu = open("zapis_z_listy.txt", "w")
plik_zapisu.writelines(lista)  # Zapis listy do pliku
plik_zapisu.close()
