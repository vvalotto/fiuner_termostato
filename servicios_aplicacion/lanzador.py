"""
Clase que inicializa el termostato
"""
from gestores_entidades.gestor_bateria import *
from gestores_entidades.gestor_ambiente import *
from gestores_entidades.gestor_climatizador import *
from servicios_aplicacion.operador_secuencial import *
from servicios_aplicacion.operador_paralelo import *
from os import system


class Lanzador:

    def __init__(self):
        self._gestor_bateria = GestorBateria()
        self._gestor_ambiente = GestorAmbiente()
        self._gestor_climatizador = GestorClimatizador()
        self._presentador = Presentador(self._gestor_bateria,
                                        self._gestor_ambiente,
                                        self._gestor_climatizador)
        self._operador_paralelo = OperadorParalelo(self._gestor_bateria,
                                                       self._gestor_ambiente,
                                                       self._gestor_climatizador)

    def ejecutar(self):

        todo_ok = True
        print("INICIO")

        self._gestor_ambiente.ambiente.temperatura_deseada = 24

        print("lee_bateria")
        self._gestor_bateria.verificar_nivel_de_carga()
        if self._gestor_bateria.obtener_indicador_de_carga() != "NORMAL": todo_ok = False

        print("lee temperatura")
        self._gestor_ambiente.leer_temperatura_ambiente()
        if self._gestor_ambiente.obtener_temperatura_ambiente() is None: todo_ok = False

        print("Muestra estado Termostato")
        self._presentador.ejecutar()

        system("clear")

        if todo_ok:
            print("Entra en operacion")
            self._operador_paralelo.ejecutar()

        return