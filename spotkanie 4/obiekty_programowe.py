# Obiekty programowe
# Tworzenie klasy


class Student(object):
    """Klasa studenta"""
    ilosc = 0

    # konstruktor klasy
    def __init__(self, imie, humor):
        print("Zapisał się nowy student")
        self.imie = imie
        self.__humor = humor
        Student.ilosc += 1

    def __str__(self):
        rep = "Obiekt klasy Student:\n"
        rep += "imie: " + self.imie + "\n"
        rep += "mój humor jest: " + self.__humor
        return rep

    # metoda klasy
    def ocena(self):
        print("Dzień dobry Panie Sajko. Mam na imie", self.imie)
        print("Pan da 3.0")

    # metoda statyczna
    @staticmethod
    def status():
        print("Ogólna liczba studentów wynosi: " + str(Student.ilosc))

    # metoda prywatna
    def __private_method(self):
        print("Metoda prywatna")

    # metoda publiczna
    def public_method(self):
        print("Metoda publiczna")
        self.__private_method()


janusz = Student("Janusz", "Dobry")
janusz.ocena()

grazynka = Student("Grażynka", "Słaby")
grazynka.ocena()

# Dostęp pośredni do metod i atrybutów prywatnych
janusz.public_method()
print(janusz)

# Dostęp bezpośredni do metod i atrybutów prywatnych
print(janusz._Student__humor)
janusz._Student__private_method()

Student.status()
