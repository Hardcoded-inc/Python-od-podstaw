# Prosta gra w karty


class Karta(object):  # klasa 1 karty
    """Karta do gry"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Reka(object):
    """Ręka gracza w karty"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for karta in self.cards:
                rep += str(karta) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, karta):
        self.cards.append(karta)

    def give(self, karta, gracz):
        self.cards.remove(karta)
        gracz.add(karta)


# Część główna programu

# tworzenie kart (ręcznie)
card1 = Karta(rank="A", suit="c")
card2 = Karta(rank="2", suit="c")
card3 = Karta(rank="3", suit="c")
card4 = Karta(rank="4", suit="c")
card5 = Karta(rank="5", suit="c")

# tworzenie graczy (ręcznie)
gracz1 = Reka()
gracz1.add(card1)
gracz1.add(card2)
gracz1.add(card3)
gracz1.add(card4)
gracz1.add(card5)

print(gracz1)

gracz2 = Reka()

print(gracz2)

gracz1.give(card1, gracz2)
gracz1.give(card2, gracz2)

print(gracz2)

