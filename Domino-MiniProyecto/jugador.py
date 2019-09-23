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
