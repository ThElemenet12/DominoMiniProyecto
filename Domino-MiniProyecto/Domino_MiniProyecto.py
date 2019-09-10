import random
import time

class Ficha:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.enTablero = False

    @property
    def _numero1(self):
        return self.numero1
    @property 
    def _numero2(self):
        return self.numero2
    
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
    def __init__(self, nombre, numeroJugador, equipo):
        self.numeroJugador =  numeroJugador
        self.fichas = []
        self.puntaje = 0
        self._nombre = nombre
        self.equipo = equipo

    def agregarFicha(self, ficha):
        self.fichas.append(ficha)
    @property
    def _equipo(self):
        return self.equipo
    @_equipo.setter
    def _equipo(self, equipo):
        self.equipo = equipo

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
        self.fichasEnTablero = []

    def colocarFicha(self, ficha, cabezaA):
        #Si cabezaA es True, se coloca en la cabezaA 
        #Si cabezaA es False, se coloca en la cabezaB
        #Si cabezaA es None, se coloca en ambas cabezas
        #Retorna True, si se coloca correctamente
    

        if(self.cabezaA == None and self.cabezaB == None):
            self.cabezaA = ficha.numero1
            self.cabezaB = ficha.numero2
            self.fichasEnTablero.append(ficha)
            return True
        else:
            if cabezaA:
                if self.cabezaA == ficha.numero1:
                    self.cabezaA = ficha.numero2
                    self.fichasEnTablero.append(ficha)
                    return True
                elif self.cabezaA == ficha.numero2:
                    self.cabezaA = ficha.numero1
                    self.fichasEnTablero.append(ficha)
                    return True
                
            else:
                if self.cabezaB == ficha.numero1:
                    self.cabezaB = ficha.numero2
                    self.fichasEnTablero.append(ficha)
                    return True
                elif self.cabezaB == ficha.numero2:
                    self.cabezaB = ficha.numero1
                    self.fichasEnTablero.append(ficha)
                    return True
        return False
    @property
    def _fichasTablero(self):
        return self.fichasEnTablero

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
        self.fichas = []
        for i in range(7):
            for j in range(i, 7):
                nuevaFicha = Ficha(j,i)
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

def verificarTranque(tablero):
    #retorna falso si el juego no esta trancado
    #retorna true si el juego esta trancado
    tranqueEnA = False
    tranqueEnB = False

    cantidadFichasPorNumero = [0,0,0,0,0,0,0]
    for x in tablero._fichasTablero:
        cantidadFichasPorNumero[x._numero1] += 1
        cantidadFichasPorNumero[x._numero2] += 1

    i = 0
    while i < 7:
        if(cantidadFichasPorNumero[i] == 8):
            if(tablero.cabezaA == i):
                tranqueEnA = True
            if(tablero.cabezaB == i):
                tranqueEnB = True
        i+= 1

    if(tranqueEnA and tranqueEnB):
        return True
    
    return False    

def asignarFichas(juego, inicio):
    i = 0
    mazoDeFichas = []
    while i < 7:
        mazoDeFichas.append(juego._fichas[inicio])
        inicio+=1
        i += 1
    return mazoDeFichas

def iniciarJuego(juego, newGame, multijugador):
    juego.crearFichas()
    juego.barajarFichas()
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
                nombrePlayer = input("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
                i+=1
                juego.agregarJugadores(Jugador(nombrePlayer,i,equipo))
                
            else:
                nombrePlayer = input("Digite el nombre del Jugador no. {}: ".format(str(i + 1)))
                i+= 1
                juego.agregarJugadores(Jugador(nombrePlayer, i, None))

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
    if(jugador._equipo != None):
        print("\n\nTurno de: {} del equipo {}".format(jugador.nombre, jugador._equipo)) 
    else:
        print("\n\nTurno de: {}".format(jugador.nombre))
    print("\nLas dos cabezas son A = {} y B = {}\n".format(str(tablero.cabezaA), str(tablero.cabezaB)))
    for x in jugador._fichas:
        print(x.dosNumero,end = ' ')
   
    i = 1
     
    while i <= len(jugador._fichas):
        if i == 1:
            print("\n {} ".format(str(i)),end = ' ')
        else:
            print(" {} ".format(str(i)),end = ' ')
        i += 1

    correcto = False
    while(not correcto):
        fichaElegida = input("\n\nEscriba un numero del 1 al {} para elegir una ficha y colocarla en el tablero... \nO presione \"Q\" para pasar: ".format(str(len(jugador._fichas))))
        if fichaElegida == "Q" or fichaElegida == "q":
            print("\nEl jugador {} paso".format(jugador.nombre))
            pasar = True
            correcto = True
            
        else: 
            try:
                fichaElegida = int(fichaElegida)
                colocado = None
                
                if int(fichaElegida) > len(jugador._fichas) or int(fichaElegida) < 1:
                    print("Error! Numero incorrercto, debe ser entre 1 y {}".format(str(len(jugador._fichas))))
                elif(tablero.cabezaA != None and tablero.cabezaB != None):
                    if(jugador._fichas[fichaElegida - 1].numero1 != tablero.cabezaA and jugador._fichas[fichaElegida - 1].numero1 != tablero.cabezaB):
                         if (jugador._fichas[fichaElegida - 1].numero2 != tablero.cabezaA and jugador._fichas[fichaElegida - 1].numero2 != tablero.cabezaB):
                            print("Error! La ficha no encaja en ninguna cabeza") 
                         else:
                             correcto = True
                    else:
                        correcto = True
                else:
                    correcto = True
            except ValueError:
                print("Error, debe ser un numero o la letra Q")
            
    if(not pasar):
        while(True):
            if(tablero.cabezaA != tablero.cabezaB):
                respuesta = input("\nEn que cabeza la colocamos? A o B: ").upper()
                if respuesta == "A":
                    cabeza = True
                elif respuesta == "B":
                    cabeza = False
                else:
                    print("Error! Digite de nuevo")
                    continue
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
            if(x is not juego._ganador):
                puntaje += y.valorPuntaje

    return puntaje
def buscarTeam(juego, equipo):
    listTeam = []
    for x in juego.getJugadores:
        if(x._equipo == equipo):
            listTeam.append(x)

    return listTeam
def jugando(juego, tope, multijugador):
    tablero = None
    ronda = 1
    orden = []
    iniciado = False
    while(True):
        print("\nRONDA no.{}".format(str(ronda)))
        time.sleep(3)
        if not iniciado:
            orden = crearOrden(juego)
            iniciado = True
            tablero = Tablero()

        turnoJugador = 0
        while(juego._ganador == None):
            juego._ganador = turno(tablero, orden[turnoJugador])
            turnoJugador += 1
            if(verificarTranque(tablero) and juego._ganador == None):
                print("\nTRANQUE!!\n")
                time.sleep(1)
                print("Buscando ganador, espere...")
                time.sleep(3)
                tantosMenor,tantos, jugadorGanador = 168,0, None
                for x in juego.getJugadores:
                    for y in x._fichas:
                        tantos += y.valorPuntaje
                    if tantos <= tantosMenor:
                        tantosMenor, tantos, juego._ganador = tantos, 0, x

            elif(turnoJugador == 4):
                turnoJugador = 0
            
        
        if(multijugador):
            teamGanador = buscarTeam(juego,juego._ganador._equipo)
            print("ENHORABUENA, LOS GANADORES DE ESTA RONDA FUERON EL EQUIPO {}: {} {}".format(juego._ganador._equipo, teamGanador[0].nombre, teamGanador[1].nombre))
            time.sleep(2)
            print("Contando los tantos, espere...")
            time.sleep(3)
            for x in juego.getJugadores:
                if(x.numeroJugador == juego._ganador._equipo):
                    x.puntaje += calcularTantos(juego)
                    juego._ganador.puntaje = x.puntaje
                    break
            
            print("El puntaje final fue de {} tantos! ".format(str(juego._ganador.puntaje)))
            time.sleep(1)
            if(juego._ganador.puntaje >= tope):
                print("EL EQUIPO {} HA GANADO EL JUEGO!".format(juego._ganador._equipo))
                break
            else:
                iniciarJuego(juego,False, multijugador)
                orden = crearOrden(juego)
                tablero = Tablero()
                juego.ganador = None
                ronda+= 1
        else:    
            print("ENHORABUENA, EL GANADOR DE ESTA RONDA FUE {}".format(juego._ganador.nombre))
            time.sleep(2)
            print("Contando los tantos, espere...")
            time.sleep(3)
            for x in juego.getJugadores:
                if(x.numeroJugador == juego._ganador.numeroJugador):
                    x.puntaje += calcularTantos(juego)
                    juego._ganador.puntaje = x.puntaje
                    break

            print("El puntaje final fue de {} tantos! ".format(str(juego._ganador.puntaje)))
            time.sleep(1)
            if(juego._ganador.puntaje >= tope):
                print("{} HA GANADO EL JUEGO!".format(juego._ganador.nombre))
                break
            else:
                iniciarJuego(juego,False, multijugador)
                orden = crearOrden(juego)
                tablero = Tablero()
                juego.ganador = None
                ronda+= 1

multijugador = False
correcto = False
while(not correcto):
    try:
        respuestaMenu = int(input("BIENVENIDO A PYTHONMINO!!! \n Como desea Jugar? \n1.Individual\n2.Equipos\nElija:"))
        if(respuestaMenu != 1 and respuestaMenu != 2):
            print("Error! Debe ser 1 o 2")
        else:
            correcto = True
    except ValueError:
        print("Error! Debe ser 1 o 2")

if respuestaMenu == 1:
    multijugador = False
else:
    multijugador = True

domino = Juego()
tablero = Tablero()
iniciarJuego(domino,True, multijugador)
jugando(domino,80, multijugador)
#for w in domino._fichas:
 #   print(w.dosNumero)
#for x in domino.getJugadores:
 #   print("\n {} sus fichas son: ".format(x.nombre), end = ' ')
  #  for y in x._fichas:
   #     print(y.dosNumero, end = ' ')
#jugando(domino)
#print("El doble 6 esta en {} ".format(buscarDobleSeis(domino).nombre))
#print(tablero.colocarFicha(Ficha(6,6),True))

