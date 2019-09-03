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
        return '{}/{}'.format(self.numero1, self.numero2)
    @property
    def _enTablero(self):
        return self.enTablero
    @_enTablero.setter
    def _enTablero(self, enTablero):
        self.enTablero = enTablero

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

    def colocarFicha(self, ficha, cabezaA):
        #Si cabezaA es True, se coloca en la cabezaA 
        #Si cabezaA es False, se coloca en la cabezaB
        #Retorna True, si se coloca correctamente

        if(cabezaA == None and cabezaB == None):
            cabezaA = ficha.numero1
            cabezaB = ficha.numero2
            return True
        else:
            if cabezaA:
                if self.cabezaA == ficha.numero1:
                    self.cabezaA = ficha.numero2
                    return True
                elif self.cabezaA == ficha.numero2:
                    self.cabezaA = ficha.numero1
                    return True
            else:
                if self.cabezaB == ficha.numero1:
                    self.cabezaB = ficha.numero2
                    return True
                elif self.cabezaB == ficha.numero2:
                    self.cabezaB = ficha.numero1
                    return True
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
    def _ganador(self):
        return self.ganador
    @_ganador.setter
    def _ganador(self,ganador):
        self.ganador = ganador

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

    juego.asignarFichas

def crearOrden(juego):
    orden = []
    index = 0
    firstPlayer = False
    while(len(orden) < 4):
        if(not firstPlayer):
            if(juego._ganador != None):
                index = juego._ganador.numeroJugador - 1
                orden.append(juego.getJugadores[index])
                firstPlayer = True
            else:
                index = buscarDobleSeis(juego).numeroJugador - 1
                orden.append(juego.getJugadores[index])
                firstPlayer = True
        else:
            if(index > 3):
                index = 0
            orden.append(juego.getJugadores[index])

        index += 1
    return orden

def buscarDobleSeis(juego):
    for x in juego.getJugadores:
        for y in x._fichas:
            if y.numero1 == 6 and y.numero2 == 6:
                return x

def turno(tablero, jugador):
    #Retorna True si el jugador gano
    #Retorna False si aun no gana 

    print("Turno de: {}".format(jugador.nombre))
    print("Las dos cabezas son A = {} y B = {}".format(str(tablero.numero1), str(tablero.numero2)))
    for x in jugador._fichas:
        print(x.dosNumero,end = ' ')

    fichaElegida = input("Escriba un numero del 1 al {} para elegir una ficha y colocarla en el tablero".format(str(len(jugador._fichas))))
    if int(fichaElegida) > len(jugador._fichas) or int(fichaElegida) < 1:
        print("Error! Numero incorrercto")
    else:
        if(jugador._fichas[fichaElegida - 1].numero1 is not tablero.cabezaA or jugador._fichas[fichaElegida - 1].numero1 is not tablero.cabezaB):
            if (jugador._fichas[fichaElegida - 1].numero2 is not tablero.cabezaA or jugador._fichas[fichaElegida - 1].numero2 is not tablero.cabezaB):
                print("Error! La ficha no encaja en ninguna cabeza")
        else:
            cabeza = input("En que cabeza la colocamos? A o B") 
            cabeza = cabeza == "A"
            if  not tablero.colocarFicha(jugador._fichas[fichaElegida - 1],cabeza):
                print("Error, no encaja en esa cabeza")
            else:
                jugador._fichas[fichaElegida -1]._enTablero = tablero.colocarFicha(jugador._fichas[fichaElegida - 1],cabeza)
                print("Ficha colocada correctamente")
                jugador._fichas.pop(fichaElegida - 1)
    if(len(jugador._fichas) == 0):
        return True
    else:
        return False

    

        


def jugando(juego):
    tablero = Tablero()
    orden = []
    iniciado = False
    while(True):
        if not iniciado:
            orden = crearOrden(juego)
            iniciado = True
            juego._ganador = None

        turno = 0
        while(juego._ganador == None):
            if(turno > 3):
                turno = 0
            tablero = turno(tablero, orden[turno])
                

            turno += 1


           




        break
        

domino = Juego()
iniciarJuego(domino)


  

 
