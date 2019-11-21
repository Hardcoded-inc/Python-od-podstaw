# Instrukcje warunkowe

liczba = int(input("Wprowadź liczbę od 1 do 4: "))

if liczba > 4:  # liczba większa od 4
    print("Błąd, liczba za duża!")
elif liczba < 1:  # liczba mniejsza od 1
    print("Błąd, liczba jest za mała")
else:  # Pozostałe przypadki
    print("Wprowadzono poprawną liczbę: ", liczba)

"""

Operatory porównania:

== Równa się np. 5 == 5 -> True
!= Nie równa się np. 5 != 5 -> False
> Większe np. 5 > 4 -> True
< Mniejsze np. 5 < 4 -> False
>= Większe/równe np. 5 >= 5 -> True
<= Mniejsze/równe np. 4 <= 5 -> True

"""