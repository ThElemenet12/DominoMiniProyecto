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



