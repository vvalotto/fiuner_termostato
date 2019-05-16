import time
from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_ambiente import *
from servicios_aplicacion.presentador import *


class Operador:

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_ambiente = GestorAmbiente()
        self._presentador = Presentador(self._gestor_bateria, self._gestor_ambiente)

    def ejecutar(self):

        print("inicio")

        while True:
            print("lee_bateria")
            self._gestor_bateria.verificar_nivel_de_carga()
            time.sleep(1)

            print("lee temperatura")
            self._gestor_ambiente.leer_temperatura_ambiente()
            time.sleep(1)

            print("Muestra estado")
            self._presentador.ejecutar()
            time.sleep(5)

        return