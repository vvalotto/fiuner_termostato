"""
Es la clase responsable de orquestar de manera ciclica
la lectura de los dispositivos externos y el accionamiento
del climatizador de acuerdo al seteo de la temperatura
ambiente.
Las responsbilidades específicas son delegadas a los gestores
y procesos correspondientes
"""

import time

from agentes_sensores.proxy_selector_temperatura import *
from agentes_sensores.proxy_seteo_temperatura import *
from agentes_sensores.proxy_sensor_temperatura import *
from agentes_sensores.proxy_bateria import *
from agentes_actuadores.visualizador_climatizador import *
from agentes_actuadores.actuador_climatizador import *
from agentes_actuadores.visualizador_temperatura import *
from agentes_actuadores.visualizador_bateria import *
from entidades.ambiente import *
from entidades.bateria import *
from entidades.climatizador import *
from servicios_dominio.controlador_climatizador import *


class OperadorSecuencial:

    def __init__(self):
        """
        Arma la dependencia con las clases con las que va
        a trabajar
        """
        self._bateria = Bateria()
        self._proxy_bateria = ProxyBateria()
        self._ambiente = Ambiente()
        self._proxy_sensor_temperatura = ProxySensorTemperatura()
        self._selector_temperatura = SelectorTemperatura()
        self._seteo_temperatura = SeteoTemperatura()
        self._climatizador = Climatizador()
        self._actuador = ActuadorClimatizador()
        self._visualizador_bateria = VisualizadorBateria()
        self._visualizador_temperatura = VisualizadorTemperaturas()
        self._visualizador_climatizador = VisualizadorClimatizador()

    def ejecutar(self):

        print("inicio")

        # Setea la temperatura deseada por defecto
        # (esta linea es temporal para la entrega 2
        self._ambiente.temperatura_deseada = 24

        'Ciclo infinito que establece la secuencia de acciones' \
        'del termostato'
        while True:
            print("lee_bateria")
            self._bateria.nivel_de_carga = self._proxy_bateria.leer_carga()
            time.sleep(1)

            print("lee temperatura")
            try:
                self._ambiente.temperatura_ambiente = self._proxy_sensor_temperatura.leer_temperatura()
            except Exception:
                self._ambiente.temperatura_ambiente = None
            time.sleep(1)

            print("revisa selector de temperatura")
            while self._selector_temperatura.obtener_selector() == "deseada":
                self._ambiente.temperatura_a_mostrar = "deseada"
                if self._ambiente.temperatura_a_mostrar == "ambiente":
                    self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
                elif self._ambiente.temperatura_a_mostrar == "deseada":
                    self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)

                opcion = self._seteo_temperatura.obtener_seteo()

                if opcion == "aumentar":
                    self._ambiente.temperatura_deseada += 1
                if opcion == "disminuir":
                    self._ambiente.temperatura_deseada -= 1
            self.ambiente.temperatura_a_mostrar = "ambiente"
            time.sleep(1)

            print("acciona climatizador")
            accion = None
            temperatura = ControladorTemperatura.comparar_temperatura(self._ambiente.temperatura_ambiente,
                                                                      self._ambiente.temperatura_deseada)
            if temperatura == "alta":
                if self._climatizador.estado == "apagado":
                    accion = "enfriar"
                elif self._climatizador.estado == "calentando":
                    accion = "apagar"
                else:
                    accion = None
            if temperatura == "baja":
                if self._climatizador.estado == "apagado":
                    accion = "calentar"
                elif self._climatizador.estado == "enfriando":
                    accion = "apagar"
                else:
                    accion = None
            print('accion:', accion)
            if accion is not None:
                self._actuador.accionar_climatizador(accion)
                self._climatizador.proximo_estado(accion)
            time.sleep(1)

            print("Muestra estado")
            print("-------------- BATERIA -------------")
            self._visualizador_bateria.mostrar_tension(self._bateria.nivel_de_carga)
            self._visualizador_bateria.mostrar_indicador(self._bateria.indicador)
            print("------------------------------------")
            print("\n")
            print("------------ TEMPERATURA ----------")
            if self._ambiente.temperatura_a_mostrar == "ambiente":
                self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_ambiente)
            elif self._ambiente.temperatura_a_mostrar == "deseada":
                self._visualizador_temperatura.mostrar_temperatura_ambiente(self._ambiente.temperatura_deseada)
            print("------------------------------------")
            print("\n")
            print("------------ CLIMATIZADOR ----------")
            elf._visualizador.mostrar_estado_climatizador(self._climatizador.estado)
            print("------------------------------------")
            print("\n")
            time.sleep(5)

        # FIN DEL BUCLE
