# -*- coding: utf-8 -*-

class Apuesta:
    ''' Esta clase define una apuesta de fútbol '''

    def __init__(self, id_apostador, goles_local, goles_visitante):
        self.id_apostador = id_apostador
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def as_string(self):
        return self.id_apostador + ": " + str(self.goles_local) + " - " + str(self.goles_visitante)
