from ficha import Ficha
from jugador import Jugador
from tablero import Tablero
import random
import time

class Juego:
    def __init__(self):
        self.fichas = []
        self.jugadores = []
        self.ganador = None

    def crearFichas(self):
        self.fichas = []
        for i in range(7):
            for j in range(i, 7):
                nuevaFicha = Ficha(j,i)
                self.fichas.append(nuevaFicha)

    def barajarFichas(self):
        random.seed(None)
        i = 0
        while(i < len(self.fichas)):
            posicionRandom = random.randint(0, len(self.fichas) -1 )
            self.fichas[i],self.fichas[posicionRandom] = self.fichas[posicionRandom], self.fichas[i]
            i += 1

    def buscarDobleSeis(self):
        for x in self.jugadores:
            for y in x._fichas:
                if y.numero1 == 6 and y.numero2 == 6:
                    return x
        return None

    def crearOrden(self):
        orden = []
        index = 0
        firstPlayer = False
        while(len(orden) < 4):
            if(not firstPlayer):
                if(self.ganador != None):
                    index = self.ganador.numeroJugador - 1
                    orden.append(self.jugadores[index])
                    firstPlayer = True
                else:
                    index = self.buscarDobleSeis().numeroJugador - 1
                    orden.append(self.jugadores[index])
                    firstPlayer = True
            else:
                if(index > 3):
                    index = 0
                orden.append(self.jugadores[index])

            index += 1
        return orden
    
    def asignarFichas(self, inicio):
        i = 0
        mazoDeFichas = []
        while i < 7:
            mazoDeFichas.append(self.fichas[inicio])
            inicio+=1
            i += 1
        return mazoDeFichas
    def iniciarJuego(self, newGame, multijugador):
        self.crearFichas()
        self.barajarFichas()
        i = 0
        inicio = 0
        equipo = 1
        if newGame:
            while(i < 4):
                if(multijugador):
                    if(i % 2 == 0):
                        equipo = 1
                    else:
                        equipo = 2
                    print("\nEquipo {} !!".format(str(equipo)))
                    correcto = False
                    while(not correcto):
                        correcto = True
                        nombrePlayer = input("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
                        for player in self.jugadores:
                            if player._nombre == nombrePlayer:
                                print("\nEl jugador ya ha sido registrado. Digite de nuevo")
                                correcto = False
                                break   
                    i+=1
                    self.jugadores.append(Jugador(nombrePlayer,i,equipo))
                
                else:
                    correcto = False
                    while(not correcto):
                        correcto = True
                        nombrePlayer = input("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
                        for player in self.jugadores:
                            if player._nombre == nombrePlayer:
                                print("\nEl jugador ya ha sido registrado. Digite de nuevo")
                                correcto = False
                                break   
                    i+= 1
                    self.jugadores.append(Jugador(nombrePlayer, i, None))

        for x in self.jugadores:
            x._fichas = self.asignarFichas(inicio)
            inicio += 7
    def calcularTantos(self):
        puntaje = 0
        for x in self.jugadores:
            for y in x._fichas:
                if(x is not self.ganador):
                    puntaje += y.valorPuntaje

        return puntaje 

    def buscarTeam(self, equipo):
        listTeam = []
        for x in self.jugadores:
            if(x._equipo == equipo):
                listTeam.append(x)

        return listTeam
    def jugando(self, tope, multijugador):
        tablero = None
        ronda = 1
        orden = []
        iniciado = False
        while(True):
            print("\nRONDA no.{}".format(str(ronda)))
            time.sleep(3)
            if not iniciado:
                orden = self.crearOrden()
                iniciado = True
                tablero = Tablero()

            turnoJugador = 0
            while(self.ganador == None):
                self.ganador = tablero.turno(orden[turnoJugador])
                turnoJugador += 1
                if(tablero.verificarTranque() and self.ganador == None):
                    print("\nTRANQUE!!\n")
                    time.sleep(1)
                    print("Buscando ganador, espere...")
                    time.sleep(3)
                    tantosMenor,tantos, jugadorGanador = 168,0, None
                    for x in self.jugadores:
                        for y in x._fichas:
                            tantos += y.valorPuntaje
                        if tantos <= tantosMenor:
                            tantosMenor, tantos, self.ganador = tantos, 0, x

                elif(turnoJugador == 4):
                    turnoJugador = 0
            
        
            if(multijugador):
                teamGanador = self.buscarTeam(self.ganador._equipo)
                print("ENHORABUENA, LOS GANADORES DE ESTA RONDA FUERON EL EQUIPO {}: {} y {}".format(self.ganador._equipo, teamGanador[0].nombre, teamGanador[1].nombre))
                time.sleep(2)
                print("Contando los tantos, espere...")
                time.sleep(3)
                for x in self.jugadores:
                    if(x.numeroJugador == self.ganador.numeroJugador):
                        calculo = self.calcularTantos()
                        print("El puntaje de la ronda fue: {}".format(str(calculo)))
                        x.puntaje += calculo
                    
                    
                        break
            
                print("El puntaje final fue de {} tantos! ".format(str(self.ganador.puntaje)))
                time.sleep(1)
                if(self.ganador.puntaje >= tope):
                    print("EL EQUIPO {} HA GANADO EL JUEGO!".format(self.ganador._equipo))
                    break
                else:
                    self.iniciarJuego(False, multijugador)
                    orden = self.crearOrden()
                    tablero = Tablero()
                    self.ganador = None
                    ronda+= 1
            else:    
                print("ENHORABUENA, EL GANADOR DE ESTA RONDA FUE {}".format(self.ganador.nombre))
                time.sleep(2)
                print("Contando los tantos, espere...")
                time.sleep(3)
                for x in self.jugadores:
                    if(x.numeroJugador == self.ganador.numeroJugador):
                        x.puntaje += self.calcularTantos()
                        self.ganador.puntaje = x.puntaje
                        break

                
                print("El puntaje total fue de {} tantos!!! ".format(str(self.ganador.puntaje)))
                time.sleep(1)
                if(self.ganador.puntaje >= tope):
                    print("{} HA GANADO EL JUEGO!".format(self.ganador.nombre))
                    break
                else:
                    self.iniciarJuego(False, multijugador)
                    orden = self.crearOrden()
                    tablero = Tablero()
                    self.ganador = None
                    ronda+= 1