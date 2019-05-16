"""

"""

import time
import threading


from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_ambiente import *
from servicios_aplicacion.presentador import *


class Operador:

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_ambiente = GestorAmbiente()
        self._presentador = Presentador(self._gestor_bateria, self._gestor_ambiente)

    def lee_carga_bateria(self):
        while True:
            print("lee_bateria")
            self._gestor_bateria.verificar_nivel_de_carga()
            time.sleep(2)
        return

    def lee_temperatura_ambiente(self):
        while True:
            print("lee temperatura")
            self._gestor_ambiente.leer_temperatura_ambiente()
            time.sleep(2)
        return

    def muestra_parametros(self):
        while True:
            self._presentador.ejecutar()
            time.sleep(5)
        return

    def ejecutar(self):


        print("inicio")

        t1 = threading.Thread(target=self.lee_carga_bateria)

        t2 = threading.Thread(target=self.lee_temperatura_ambiente)

        t3 = threading.Thread(target=self.muestra_parametros)

        t1.start()
        t2.start()
        time.sleep(10)
        t3.start()

        return

