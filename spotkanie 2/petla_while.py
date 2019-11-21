# Pętla while


# Pętle skończone

odp = ""
while odp != "2":
    odp = input("Wpisz 2: ")


# Pętle nieskończone

liczba = 0
while True:
    if liczba > 10:
        break  # Zerwanie pętli
    elif liczba == 5:
        liczba += 1
        continue  # Przejście do kolejnej iteracji
    print(liczba)
    liczba += 1
