
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
    def __init__(self, nombre, numeroJugador):
        self.numeroJugador =  numeroJugador
        self.fichas = []
        self.puntaje = 0
        self._nombre = nombre

    def agregarFicha(self, ficha):
        self.fichas.append(ficha)

    @property
    def _numeroJugador(self):
        return self.numeroJugador

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
        self.ganador = None

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

def iniciarJuego(juego):
    i = 0
    while(i < 4):
        print("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
        nombrePlayer = input()
        i+= 1
        juego.agregarJugadores(Jugador(nombrePlayer, i))

def jugando(juego):
    tablero = Tablero()
    while(True):


        break
        


domino = Juego()
iniciarJuego(juego)


  

 
