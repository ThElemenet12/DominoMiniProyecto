class Ficha:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    @property
    def valorPuntaje(self):
        return self.numero1 + self.numero2
    @property 
    def dosNumero(self):
        return '{} | {}'.format(self.numero1, self.numero2)


class Jugador:
    def __init__(self, nombre, fichas):
        self.fichas = fichas
        self.puntaje = 0
        self._nombre = nombre
        self.enTablero = False
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def enTablero(self):
        return enTablero

    @enTablero.setter
    def enTablero(self, enTablero):
        self.enTablero = enTablero

class Juego:
    def __init__(self):
        self.fichas = []
        self.jugadores = []
        self.ganador = ""

    def crearFichas(self):
        for i in range(7):
            for j in range(i, 7):
                nuevaFicha = Ficha(i,j)
                self.fichas.append(nuevaFicha)
    @property
    def _fichas(self):
        return self.fichas


jueguito = Juego()
jueguito.crearFichas()

for x in jueguito._fichas:
    print(x.dosNumero)