
from ficha import Ficha
from jugador import Jugador
from juego import Juego
from tablero import Tablero

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
domino.iniciarJuego(True, multijugador)
domino.jugando(80, multijugador)
