# Pętla for

slowo = input("Wprowadź słowo: ")
litery = 0

for litera in slowo:  # Iteracja po literach
    litery += 1
print("Wprowadziłeś słowo: ", slowo, ", które ma", litery, " liter.")
print("Wprowadziłeś słowo: ", slowo, ", które ma", len(slowo), " liter.")

for i in range(10):  # Iteracja w zakresie <0, 10)
    print(i)

for i in range(10, 100, 2):  # Iteracja w zakresie <10, 100) co 2
    print(i)

for i in range(10, 0, -1):  # Iteracja w zakresie <10, 0) odejmowanie co 1
    print(i)
