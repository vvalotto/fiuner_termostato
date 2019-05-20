"""
Clase que es la responsable de manejar la entidad Ambiente.
- Obteniendo la temperatura desde el sensor externo
- Aceptando la determinación de la temperatura deseeada
- mostrando las temperaturas en los dispositivos de visualizacion
"""

from configurador.configurador import *
from entidades.ambiente import *


class GestorAmbiente:

    @property
    def ambiente(self):
        return self._ambiente

    def __init__(self):
        self._ambiente = Ambiente()
        self._proxy_sensor_temperatura = Configurador().configurar_proxy_temperatura()
        self._visualizador_temperatura = Configurador().configurar_visualizador_temperaturas()
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
        self._ambiente.temperatura_deseada += 1
        return

    def disminuir_temperatura_deseada(self):
        self._ambiente.temperatura_deseada -= 1
        return

    def obtener_temperatura_deseada(self):
        return self._ambiente.temperatura_deseada

    def mostrar_temperatura_deseada(self):
        self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)
        return

    def mostrar_temperatura(self):
        if self._ambiente.temperatura_a_mostrar == "ambiente":
            self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
        elif self._ambiente.temperatura_a_mostrar == "deseada":
            self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)
        return

    def indicar_temperatura_a_mostrar(self, tipo_temperatura):
        self.ambiente.temperatura_a_mostrar = tipo_temperatura
        return

