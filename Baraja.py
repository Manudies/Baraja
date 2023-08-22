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
        print("Baraja completa")
        for carta in self.mazo:
            print(carta)
        print("------------")

    def barajar_mazo(self):
        self.mazo_barajado = []
        self.mazo_barajado = sorted(
            self.mazo, key=lambda y: random.randint(0, len(self.mazo)))

    def mostrar_mazo_barajado(self):
        print("Baraja barajada")
        for carta in self.mazo_barajado:
            print(carta)
        print("------------")

    def repartir_cartas(self):
        self.j1 = []
        self.j2 = []
        self.j3 = []
        self.j4 = []
        self.jugadores = []
        for i in range(5):
            carta1 = self.mazo_barajado.pop(0)
            self.j1.append(carta1)
            carta2 = self.mazo_barajado.pop(0)
            self.j2.append(carta2)
            carta3 = self.mazo_barajado.pop(0)
            self.j3.append(carta3)
            carta4 = self.mazo_barajado.pop(0)
            self.j4.append(carta4)
        self.jugadores = self.j1 + self.j2 + self.j3 + self.j4

    def mostrar_resto_mazo(self):
        print("Resto de la baraja")
        for carta in self.mazo_barajado:
            print(carta)
        print("------------")

    def mostrar_cartas_jugadores(self):
        print("Mano de los jugadores")
        print("Jugador 1: ",)
        for carta in self.j1:
            print(carta)
        print("------------")
        print("Jugador 2: ",)
        for carta in self.j2:
            print(carta)
        print("------------")
        print("Jugador 3: ",)
        for carta in self.j3:
            print(carta)
        print("------------")
        print("Jugador 4: ",)
        for carta in self.j4:
            print(carta)
        print("------------")


baraja = Baraja()
baraja.mostrar_baraja()
baraja.barajar_mazo()
baraja.mostrar_mazo_barajado()
baraja.repartir_cartas()
baraja.mostrar_resto_mazo()
baraja.mostrar_cartas_jugadores()
