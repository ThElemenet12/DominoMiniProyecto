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
    
    def verificarTranque(self):
    #retorna falso si el juego no esta trancado
    #retorna true si el juego esta trancado
        tranqueEnA = False
        tranqueEnB = False

        cantidadFichasPorNumero = [0,0,0,0,0,0,0]
        for x in self.fichasEnTablero:
            cantidadFichasPorNumero[x._numero1] += 1
            cantidadFichasPorNumero[x._numero2] += 1

        i = 0
        while i < 7:
            if(cantidadFichasPorNumero[i] == 8):
                if(self.cabezaA == i):
                    tranqueEnA = True
                if(self.cabezaB == i):
                    tranqueEnB = True
            i+= 1

        if(tranqueEnA and tranqueEnB):
            return True
    
        return False
    def turno(self, jugador):
        #Retorna el jugador si el jugador gano
        #Retorna None si aun no gana 
        pasar = False
        if(jugador._equipo != None):
            print("\n\nTurno de: {} del equipo {}".format(jugador.nombre, jugador._equipo)) 
        else:
            print("\n\nTurno de: {}".format(jugador.nombre))
        print("\nLas dos cabezas son A = {} y B = {}\n".format(str(self.cabezaA), str(self.cabezaB)))
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
                    elif(self.cabezaA != None and self.cabezaB != None):
                        if(jugador._fichas[fichaElegida - 1].numero1 != self.cabezaA and 
                           jugador._fichas[fichaElegida - 1].numero1 != self.cabezaB):
                             if (jugador._fichas[fichaElegida - 1].numero2 != self.cabezaA and 
                                 jugador._fichas[fichaElegida - 1].numero2 != self.cabezaB):
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
                if(len(jugador._fichas) == 1):
                    if(jugador._fichas[fichaElegida - 1].numero1 == self.cabezaA or 
                       jugador._fichas[fichaElegida - 1].numero2 == self.cabezaA):
                        cabeza = True
                    elif(jugador._fichas[fichaElegida - 1].numero1 == self.cabezaB or 
                         jugador._fichas[fichaElegida - 1].numero2 == self.cabezaB):
                        cabeza = False
                elif(self.cabezaA != self.cabezaB):
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

                colocado =  self.colocarFicha(jugador._fichas[fichaElegida - 1],cabeza)
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