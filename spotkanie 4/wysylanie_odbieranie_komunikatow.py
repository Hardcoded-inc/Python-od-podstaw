# Wysyłanie i odbieranie komunikatów
class Gracz(object):
    def strzelaj(self, wrog):
        print("Gracz strzela do wroga")
        wrog.umieraj()


class Wrog(object):
    def umieraj(self):
        print("Wróg umiera")


gracz = Gracz()
alien = Wrog()
gracz.strzelaj(alien)
