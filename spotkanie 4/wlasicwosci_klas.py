# Właściwości klas


class Student(object):
    """Studect CDV"""

    # konstruktor klasy
    def __init__(self, imie):
        print("Zapisał się nowy student!")
        self.__imie = imie

    # Właściwość
    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, new_name):
        if new_name == "":
            print("Imię nie może być puste!")
        else:
            self.__imie = new_name
            print("Zmieniono imię.")

    def przedstawienie(self):
        print("Cześć, jestem", self.__imie)


# Dostęp do właściwości
janusz = Student("Janusz")
janusz.przedstawienie()
print(janusz.imie)

print("Spróbujemy zmienić imię studenta na \"Grażynka\"")
janusz.imie = "Grazynka"

print("Imie naszego studenta to", end=" ")
print(janusz.imie)
