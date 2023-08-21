import random


class Carta:

    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return "[{}-{}]".format(self.numero, self.palo)


class Baraja:

    def __init__(self):
        palos = ["O", "C", "E", "B"]
        numeros = ["As", 2, 3, 4, 5, 6, 7, "S", "C", "R"]

        self.mazo = []
        self.mazo_barajado = []
        for n in numeros:
            for p in palos:
                carta = Carta(n, p)
                self.mazo.append(carta)

    def mostrar_baraja(self):
        for carta in self.mazo:
            print(carta)

    def barajar_mazo(self):
        self.mazo_barajado = []
        self.mazo_barajado = sorted(
            self.mazo, key=lambda y: random.randint(0, len(self.mazo)))

    def mostrar_mazo_barajado(self):
        for carta in self.mazo_barajado:
            print(carta)


# baraja = Baraja()
# baraja.mostrar_baraja()
# baraja.barajar_mazo()
# baraja.mostrar_mazo_barajado()
