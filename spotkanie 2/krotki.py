# Krotki (tuple)

pusta_krotka = ()  # Tworzy pustą krotkę

pelna_krotka = (
    "tekst",
    1,
    2.5,
    (),
    (2, 5, "tekst")
)  # Tworzy pełną krotkę

if not pusta_krotka:  # Jeżeli krotka pusta
    print("Krotka jest pusta")
print(pusta_krotka)

if pelna_krotka:  # Jeżeli krotka nie pusta
    print("Krotka nie jest pusta")
print(pelna_krotka)

for element in pelna_krotka:
    print(element)  # Wypisz każdy element krotki

# Wypisywanie poszczególnych indeksów
print(pelna_krotka[0])
print(pelna_krotka[1])
print(pelna_krotka[2])
print(pelna_krotka[3])
print(pelna_krotka[4])

