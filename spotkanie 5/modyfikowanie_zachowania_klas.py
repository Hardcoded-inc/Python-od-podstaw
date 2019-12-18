# Modyfikowanie zachowania odziedziczonych klas


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


class Talia(Reka):
    """Talia kart"""
    def popolate(self):
        for suit in Karta.SUITS:
            for rank in Karta.RANKS:
                self.add(Karta(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę już rozdawać. Brak kart.")


class ZakrytaKarta(Karta):
    """Wyświetli zakrytą kartę"""
    def __str__(self):
        return "<zakryta>"

# część główna


deck = Talia()
print(deck)
deck.popolate()
print(deck)
deck.shuffle()
print(deck)

gracz1 = Reka()
gracz2 = Reka()

gracze = [gracz1, gracz2]

deck.deal(gracze, per_hand=5)

print(gracz1)
print(gracz2)

