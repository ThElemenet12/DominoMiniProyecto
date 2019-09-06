import random

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
    @_fichas.setter
    def _fichas(self, fichas):
        self.fichas = fichas

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
        #Si cabezaA es None, se coloca en ambas cabezas
        #Retorna True, si se coloca correctamente

        if(self.cabezaA == None and self.cabezaB == None):
            self.cabezaA = ficha.numero1
            self.cabezaB = ficha.numero2
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

    def barajarFichas(juego):
        random.seed(None)
        i = 0
        while(i < len(juego._fichas)):
            posicionRandom = random.randint(0, len(juego._fichas) -1 )
            juego._fichas[i],juego._fichas[posicionRandom] = juego._fichas[posicionRandom], juego._fichas[i]
            i += 1

                
    @property
    def _ganador(self):
        return self.ganador
    @_ganador.setter
    def _ganador(self,ganador):
        self.ganador = ganador

    @property
    def _fichas(self):
        return self.fichas
    @_fichas.setter
    def _fichas(self,fichas):
        self.fichas = fichas
    
    @property
    def getJugadores(self):
        return self.jugadores
  

    def agregarJugadores(self, jugador):
        self.jugadores.append(jugador)


def asignarFichas(juego, inicio):
    i = 0
    mazoDeFichas = []
    while i < 7:
        mazoDeFichas.append(juego._fichas[inicio])
        inicio+=1
        i += 1
    return mazoDeFichas

def iniciarJuego(juego, newGame):
    juego.crearFichas()
    juego.barajarFichas()
    i = 0
    inicio = 0
    if newGame:
        while(i < 4):
            nombrePlayer = input("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
            i+= 1
            juego.agregarJugadores(Jugador(nombrePlayer, i))

    for x in juego.getJugadores:
        x._fichas = asignarFichas(juego,inicio)
        inicio += 7
        
def buscarDobleSeis(juego):
    for x in juego.getJugadores:
        for y in x._fichas:
            if y.numero1 == 6 and y.numero2 == 6:
                return x
    return None

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

def turno(tablero, jugador):
    #Retorna el jugador si el jugador gano
    #Retorna None si aun no gana 
    pasar = False
    print("\n\nTurno de: {}".format(jugador.nombre))
    print("\nLas dos cabezas son A = {} y B = {}".format(str(tablero.cabezaA), str(tablero.cabezaB)))
    for x in jugador._fichas:
        print(x.dosNumero,end = ' ')

    while(True):
        fichaElegida = input("Escriba un numero del 1 al {} para elegir una ficha y colocarla en el tablero... \nO presione \"Q\" para pasar: ".format(str(len(jugador._fichas))))
        if fichaElegida == "Q" or fichaElegida == "q":
            print("\nEl jugador {} paso".format(jugador.nombre))
            pasar = True
            break
        else: 
            fichaElegida = int(fichaElegida)
            colocado = None
            if int(fichaElegida) > len(jugador._fichas) or int(fichaElegida) < 1:
                print("Error! Numero incorrercto")
            elif(tablero.cabezaA != None and tablero.cabezaB != None):
                if(jugador._fichas[fichaElegida - 1].numero1 != tablero.cabezaA and jugador._fichas[fichaElegida - 1].numero1 != tablero.cabezaB):
                     if (jugador._fichas[fichaElegida - 1].numero2 != tablero.cabezaA and jugador._fichas[fichaElegida - 1].numero2 != tablero.cabezaB):
                        print("Error! La ficha no encaja en ninguna cabeza") 
                     else:
                         break
                else:
                    break
            else:
                break
    if(not pasar):
        while(True):
            if(tablero.cabezaA != None and tablero.cabezaB != None):
                respuesta = input("\nEn que cabeza la colocamos? A o B: ").upper()
                cabeza = True if respuesta == "A" else False
            else:
                cabeza = None

            colocado =  tablero.colocarFicha(jugador._fichas[fichaElegida - 1],cabeza)
            if  not colocado:
                print("Error, no encaja en esa cabeza ")
            else: 
                break

        jugador._fichas[fichaElegida -1]._enTablero = True
        print("Ficha colocada correctamente")
        jugador._fichas.pop(fichaElegida - 1)

    if(len(jugador._fichas) == 0):
        return jugador
    else:
        return None
def calcularTantos(juego):
    puntaje = 0
    for x in juego.getJugadores:
        for y in x._fichas:
            puntaje += y.valorPuntaje

    return puntaje
def jugando(juego, tope):
    tablero = None
    orden = []
    iniciado = False
    while(True):
        if not iniciado:
            orden = crearOrden(juego)
            iniciado = True
            tablero = Tablero()

        turnoJugador = 0
        while(juego._ganador == None):
            juego._ganador = turno(tablero, orden[turnoJugador])
            turnoJugador += 1
            if(turnoJugador == 4):
                turnoJugador = 0
        print("ENHORABUENA, EL GANADOR DE ESTA RONDA FUE {}".format(juego._ganador.nombre))
        
        for x in juego.getJugadores:
            if(x.numeroJugador == juego._ganador.numeroJugador):
                x.puntaje = calcularTantos(juego)
                juego._ganador.puntaje = x.puntaje
                break

        print("El puntaje final fue de {} tantos! ".format(str(juego._ganador.puntaje)))
        if(juego._ganador.puntaje >= tope):
            print("{} HA GANADO EL JUEGO!".format(juego._ganador.nombre))
            break
        else:
            iniciarJuego(juego,False)
            orden = crearOrden(juego)
            tablero = Tablero()
            juego.ganador = None
            
domino = Juego()
tablero = Tablero()
iniciarJuego(domino,True)
jugando(domino,100)
#for w in domino._fichas:
 #   print(w.dosNumero)
#for x in domino.getJugadores:
 #   print("\n {} sus fichas son: ".format(x.nombre), end = ' ')
  #  for y in x._fichas:
   #     print(y.dosNumero, end = ' ')
#jugando(domino)
#print("El doble 6 esta en {} ".format(buscarDobleSeis(domino).nombre))
#print(tablero.colocarFicha(Ficha(6,6),True))

 
