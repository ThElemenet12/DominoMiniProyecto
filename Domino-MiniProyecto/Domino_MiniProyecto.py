
from random import seed
from random import randint

class Ficha:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.enTablero = False

    @property
    def valorPuntaje(self):
        return self.numero1 + self.numero2
    @property 
    def dosNumero(self):
        return '{} | {}'.format(self.numero1, self.numero2)
    
    @property
    def enTablero(self):
        return enTablero

    @enTablero.setter
    def enTablero(self, enTablero):
        self.enTablero = enTablero


class Jugador:
    def __init__(self, nombre):
        self.fichas = []
        self.puntaje = 0
        self._nombre = nombre

    def agregarFicha(self, ficha):
        self.fichas.append(ficha)

    @property
    def _fichas(self):
        return self.fichas

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
   

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
    def barajarFichas(self):
        seed(1)
        i = 0

        while(i < len(self.fichas)):
            jugadorActual = self.jugadores[randint(0,4)]
            if(len(jugadorActual._fichas) < 7):
                jugadorActual.agregarFicha(self.fichas(i))
                i+= 1
                
    @property
    def _fichas(self):
        return self.fichas
    
    @property
    def getJugadores(self):
        return self.jugadores
  

    def agregarJugadores(self, jugador):
        self.jugadores.append(jugador)

jueguito = Juego()
jugador1 = Jugador("Pedro")


