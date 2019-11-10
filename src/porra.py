from partido import Partido
from partido import EstadoPartido

class Porra:
    '''
    Esta clase define una porra, la cual tendrá un partido asociado
    y una lista de apuestas asociado a dicho partido
    '''

    def __init__(self, partido):
        self.partido = partido
        self.nombre_porra = partido.nombre
        self.apuestas = []


    def consultar_estado_apuesta(self, id_apostador):
        """
        Método para consultar el estado de la apuesta de un id_apostador
        :param id_apostador: identificador del apostador
        :return: estado de la apuesta asociada a id_apostador
        """

        for apuesta in self.apuestas:
            if apuesta.id_apostador == id_apostador:
                if self.partido.estado == EstadoPartido.FINALIZADO:
                    if apuesta.goles_local == self.partido.goles_local and apuesta.goles_visitante == self.partido.goles_visitante:
                        return id_apostador + " has ganado la porra."
                    else:
                        return id_apostador + " has perdido la porra."
                else:
                    return self.partido.estado

        return "Error: " + id_apostador + " no tiene una apuesta asociada a esta porra."


    def consultar_informacion_apuesta(self, id_apostador):
        """
        Método para consultar la información de la apuesta
        :param id_apostador: identificador del id_apostador
        :return: información de la apuesta asociada a id_apostador
        """

        for apuesta in self.apuestas:
            if apuesta.id_apostador == id_apostador:
                return apuesta.as_string()

        return "Error: " + id_apostador + " no tiene una apuesta asociada a esta porra."


    def as_string(self):
        """
        :return: devuelve el nombre de la porra y todas las apuestas de dicha porra
        """
        cadena = self.nombre_porra + "\n"

        for apuesta in self.apuestas:
            cadena += apuesta.as_string() + "\n"

        return cadena


    def comenzar_partido(self):
        """
        Método para cambiar el estado del partido a EN_JUEGO
        :return: resultado de la operación
        """
        return self.partido.comenzar_partido()


    def finalizar_partido(self):
        """
        Método para cambiar el estado del partido a FINALIZADO
        :return: resultado de la operación
        """
        return self.partido.finalizar_partido()


    def nueva_apuesta(self, apuesta):
        """
        Método para agregar una nueva apuesta a la lista
        :param apuesta: apuesta que se va a agregar a la lista de apuestas
        :return: resultado de la operación
        """

        if self.partido.estado == EstadoPartido.EN_JUEGO:
            return "Error: no se puede agregar la apuesta, el partido ya está en juego."

        if self.partido.estado == EstadoPartido.FINALIZADO:
            return "Error: no se puede agregar la apuesta, el partido ya ha finalizado."

        for a in self.apuestas:
            if a.id_apostador == apuesta.id_apostador:
                return "Error: ya existe una apuesta asociada al apostador."

        if isinstance(apuesta, Apuesta):
            self.apuestas.append(apuesta)
            return "Apuesta agregada correctamente."
        else:
            return "Error: tipo de apuesta inválido."


    def modificar_apuesta(self, apuesta):
        """
        Método para modificar una apuesta de la lista
        :param apuesta: apuesta con los datos nuevos
        :return: resultado de la operación
        """

        if not isinstance(apuesta, Apuesta):
            return "Error: tipo de apuesta inválido."

        if self.partido.estado == EstadoPartido.EN_JUEGO:
            return "Error: no se puede modificar la apuesta, el partido ya está en juego."

        if self.partido.estado == EstadoPartido.FINALIZADO:
            return "Error: no se puede modificar la apuesta, el partido ya ha finalizado."

        for i in range(0, len(self.apuestas)):
            if self.apuestas[i].id_apostador == apuesta.id_apostador:
                self.apuestas[i].goles_local = apuesta.goles_local
                self.apuestas[i].goles_visitante = apuesta.goles_visitante
                return "Apuesta modificada correctamente."

        return "Error: el apostador no tenía ninguna apuesta."
