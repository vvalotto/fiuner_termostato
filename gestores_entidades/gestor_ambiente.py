"""
Clase que es la responsable de manejar la entidad Ambiente.
- Obteniendo la temperatura desde el sensor externo
- Aceptando la determinación de la temperatura deseeada
- mostrando las temperaturas en los dispositivos de visualizacion
"""

from agentes_sensores.proxy_sensor_temperatura import *
from entidades.ambiente import *
from agentes_actuadores.visualizador_temperatura import *


class GestorAmbiente:

    def __init__(self):
        self._ambiente = Ambiente()
        self._proxy_sensor_temperatura = ProxySensorTemperatura()
        self._visualizador_temperatura = VisualizadorTemperaturas()
        return

    def leer_temperatura_ambiente(self):
        try:
            self._ambiente.temperatura_ambiente = self._proxy_sensor_temperatura.leer_temperatura()
        except Exception:
            self._ambiente.temperatura_ambiente = None
        return

    def obtener_temperatura_ambiente(self):
        return self._ambiente.temperatura_ambiente

    def mostrar_temperatura_ambiente(self):
        self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
        return

    def aumentar_temperatura_deseada(self):
        return

    def disminuir_temperatura_deseada(self):
        return

    def obtener_temperatura_deseada(self):
        return

    def mostrar_temperatura_deseada(self):
        return
