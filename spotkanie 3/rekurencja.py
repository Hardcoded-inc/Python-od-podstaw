# Rekurencja
def silnia(x):
    """Oblicza silnie x"""
    if x == 0: return 1  # Zwrot wartości 1 dla x == 0
    elif x == 1: return 1  # Zwrot wartości
    else: return x * silnia(x-1)  # Dla innych wartopści odwołanie do funkcji


print(silnia(0))
print(silnia(1))
print(silnia(2))
print(silnia(3))
print(silnia(4))
print(silnia(5))
print(silnia(100))
