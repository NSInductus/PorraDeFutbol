import pytest
import sys
sys.path.append('src')
sys.path.append('../src')

from partido import Partido
from apuesta import Apuesta
from porra import Porra

texto_porra = """Madrid-Barcelona Liga 2019
Solano: 3 - 1
Angel: 2 - 1
"""

apuesta_correcta = "Apuesta agregada correctamente."
porra_en_juego = "Estado modificado a en juego."
porra_finalizada = "Estado modificado a finalizado."

error_en_juego = "Error: no se puede agregar la apuesta, el partido ya está en juego."
error_finalizado = "Error: no se puede agregar la apuesta, el partido ya ha finalizado."


def test_porra():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")
    apuesta1 = Apuesta("Solano",3,1)
    apuesta2 = Apuesta("Angel",2,1)
    porra1 = Porra(partido1)

    mensaje1 = porra1.nueva_apuesta(apuesta1)
    assert mensaje1 == apuesta_correcta

    mensaje2 = porra1.nueva_apuesta(apuesta2)
    assert mensaje2 == apuesta_correcta

    assert porra1.as_string() == texto_porra


def test_porra_en_juego():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")

    apuesta1 = Apuesta("Solano",3,1)

    porra1 = Porra(partido1)
    mensaje1 = porra1.comenzar_partido()
    assert mensaje1 == porra_en_juego

    mensaje2 = porra1.nueva_apuesta(apuesta1)
    assert mensaje2 == error_en_juego


def test_porra_finalizada():
    partido1 = Partido("Madrid", "Barcelona", "Liga", "2019")

    apuesta1 = Apuesta("Solano",3,1)

    porra1 = Porra(partido1)
    mensaje1 = porra1.comenzar_partido()
    mensaje1 = porra1.finalizar_partido()
    assert mensaje1 == porra_finalizada

    mensaje2 = porra1.nueva_apuesta(apuesta1)
    assert mensaje2 == error_finalizado
