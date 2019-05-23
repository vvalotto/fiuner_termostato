"""
Es el componente responsable de mantener y gestionar el
estado interno de la clase que representa la bateria real
"""

from entidades.bateria import *
from configurador.configurador import *


class GestorBateria:

    def __init__(self):
        """
        Inicializa el gestor que esta compuesto de:
        La clase que que obtiene la carga de la bateria desde la interfaz
        la clase que guarda el estado de la bateria
        la clase que expone visualmente el estado de la bateria
        """
        self._bateria = Bateria(5, 0.80)
        self._proxy_bateria = Configurador().configurar_proxy_bateria()
        self._visualizador_bateria = Configurador.configurar_visualizador_bateria()
        return

    def verificar_nivel_de_carga(self):
        self._bateria.nivel_de_carga = self._proxy_bateria.leer_carga()
        return

    def obtener_nivel_de_carga(self):
        return self._bateria.nivel_de_carga

    def obtener_indicador_de_carga(self):
        return self._bateria.indicador

    def mostrar_nivel_de_carga(self):
        self._visualizador_bateria.mostrar_tension(self._bateria.nivel_de_carga)
        return

    def mostrar_indicador_de_carga(self):
        self._visualizador_bateria.mostrar_indicador(self._bateria.indicador)
