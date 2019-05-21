""""
Clase que respresenta el climatizador
"""

from servicios_dominio.controlador_climatizador import *


class Climatizador:

    @property
    def estado(self):
        return self._estado

    def __init__(self):
        self._estado = "apagado"
        self._maquina_estado = []
        self._inicializar_maquina_estado()
        self._funcionamiento_acumulado = 0
        self._inicio_funcionamiento = None
        return

    def proximo_estado(self, accion):
        estado_actual = [self._estado, accion]

        for transicion in self._maquina_estado:
            if estado_actual == transicion[0]:
                self._estado = transicion[1]
                return self._estado

        raise("No existe proximo estado")
        return

    def _inicializar_maquina_estado(self):
        self._maquina_estado.append([["apagado", "calentar"], "calentando"])
        self._maquina_estado.append([["apagado", "enfriar"], "enfriando"])
        self._maquina_estado.append([["calentando", "apagar"], "apagado"])
        self._maquina_estado.append([["enfriando", "apagar"], "apagado"])
        return

    def evaluar_accion(self, ambiente):
        """
        Este metodo es muy problematico!!!
        Evalua el tipo para decidir como debe comportarse!!
        """
        if isinstance(self, Climatizador):
            if self._funcionamiento_acumulado < 120:
                temperatura = ControladorTemperatura.comparar_temperatura(ambiente.temperatura_ambiente,
                                                                          ambiente.temperatura_deseada)
                accion = self._definir_accion(temperatura)
                self._acumular_funcionamiento(accion)
            else:
                accion = "apagar"
                self._funcionamiento_acumulado = 0
                self._inicio_funcionamiento = None

        elif isinstance(self, Calefactor):
            temperatura = ControladorTemperatura.comparar_temperatura(ambiente.temperatura_ambiente,
                                                                      ambiente.temperatura_deseada)
            accion = self._definir_accion(temperatura)
        return accion

    def _definir_accion(self, temperatura):
        if temperatura == "alta":
            if self._estado == "apagado":
                accion = "enfriar"
            elif self._estado == "calentando":
                accion = "apagar"
            else:
                accion = None
        if temperatura == "baja":
            if self._estado == "apagado":
                accion = "calentar"
            elif self._estado == "enfriando":
                accion = "apagar"
            else:
                accion = None
        print('accion:', accion)
        return accion

    def _acumular_funcionamiento(self, accion):
        """
        Cuerpo del metodo
        """
        return


class Calefactor(Climatizador):

    # sobreescribe el metodo que especializa
    def _inicializar_maquina_estado(self):
        self._maquina_estado.append([["apagado", "calentar"], "calentando"])
        self._maquina_estado.append([["apagado", "enfriar"], "apagado"])
        self._maquina_estado.append([["calentando", "apagar"], "apagado"])
        return

    def _definir_accion(self, temperatura):
        accion = None
        if temperatura == "baja":
            if self._estado == "apagado":
                accion = "calentar"
        else:
            if self._estado == "calentando":
                accion = "apagar"
        print('accion:', accion)
        return accion