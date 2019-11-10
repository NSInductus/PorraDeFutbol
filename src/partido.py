from enum import Enum

class EstadoPartido(Enum):
    NO_COMENZADO = "no comenzado"
    EN_JUEGO = "en juego"
    FINALIZADO = "finalizado"


class Partido:
    ''' Esta clase define un partido de fútbol '''

    def __init__(self,  equipo_local, equipo_visitante, competicion, anio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.competicion = competicion
        self.anio = anio
        self.nombre = self.equipo_local + "-" + self.equipo_visitante + " " + self.competicion + " " + self.anio
        self.estado = EstadoPartido.NO_COMENZADO
        self.goles_local = 0
        self.goles_visitante = 0

    def comenzar_partido(self):
        if self.estado == EstadoPartido.NO_COMENZADO:
            self.estado = EstadoPartido.EN_JUEGO
            return "Estado modificado a en juego."
        else:
            return "Para modificar a en \'en juego\' es necesario que no haya comenzado."

    def finalizar_partido(self):
        if self.estado == EstadoPartido.EN_JUEGO:
            self.estado = EstadoPartido.FINALIZADO
            return "Estado modificado a finalizado."
        else:
            return "Para moficar a \'finalizado\' es necesario estar en juego."
