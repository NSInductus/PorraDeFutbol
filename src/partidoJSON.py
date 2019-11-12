# -*- coding: utf-8 -*-

import json
import sys, os.path

from partido import EstadoPartido

class PartidoJSON:

    def __init__ (self, path):

        with open(path, 'r') as f:
            partido = json.load(f)

        self.equipo_local = partido['equipo_local']
        self.equipo_visitante = partido['equipo_visitante']
        self.competicion = partido['competicion']
        self.anio = partido['anio']
        self.nombre = self.equipo_local + "-" + self.equipo_visitante + " " + self.competicion + " " + self.anio
