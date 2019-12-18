# Klasy bazowe gry


class Player(object):
    """Gracz"""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep


def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie"""
    rep = None
    while rep not in ("t", "n"):
        rep = input(question).lower()
    return rep


def ask_number(question, low, high):
    """Prosi o podanie liczby z zakresu"""
    rep = None
    while rep not in range(low, high):
        rep = int(input(question))
    return rep


if __name__ == "__main__":
    print("Uruchomiłeś moduł zamiast go zaimportować")
    input("Aby zakończyć, naciśnij Enter.")
