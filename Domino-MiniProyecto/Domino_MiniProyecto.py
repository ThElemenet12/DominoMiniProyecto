
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
    
class Tablero:
    def __init__(self):
        self.cabezaA = None
        self.cabezaB = None
        self.turno = None

    def colocarFicha(self, ficha):
        if(cabezaA == None and cabezaB == None):
            cabezaA = ficha.numero1
            cabezaB = ficha.numero2
            return True
        else:
            if self.cabezaA == ficha.numero1:
                self.cabezaA = ficha.numero2
                return True
            elif self.cabezaA == ficha.numero2:
                self.cabezaA = ficha.numero1
                return True
            elif self.cabezaB == ficha.numero1:
                self.cabezaB = ficha.numero2
                return True
            elif self.cabezaB == ficha.numero2:
                self.cabezaB = ficha.numero1
                return True
            else:
                return False
    @property
    def getCabezaA(self):
        return self.cabezaA

    @property
    def getCabezaB(self):
        return self.cabezaB
  
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
            posicionRandom = randint(0, len(self.fichas) -1 )
            self.fichas[i],self.fichas[posicionRandom] = self.fichas[posicionRandom], self.fichas[i]
            i += 1

    def asignarFichas(self):
        self.barajarFichas()
        for x in self.jugadores:
            for y in self.fichas:
                if(len(x._fichas) < 7):
                    x.agregarFicha(y)
                else:
                    break
                
     
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
jugador2 = Jugador("Juana")
jugador3 = Jugador("Marco")
jugador4 = Jugador("Polo")

jueguito.agregarJugadores(jugador1)
jueguito.agregarJugadores(jugador2)
jueguito.agregarJugadores(jugador3)
jueguito.agregarJugadores(jugador4)

jueguito.crearFichas()
jueguito.barajarFichas()

jueguito.asignarFichas()

for x in jueguito.getJugadores:
    for y in x._fichas:
        print("{} {}".format(x.nombre, y.dosNumero))