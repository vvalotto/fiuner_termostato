""""
Clase que respresenta el climatizador
"""


class Climatizador:

    @property
    def estado(self):
        return self._estado

    def __init__(self):
        self._estado = "apagado"
        self._maquina_estado = []
        self._inicializar_maquina_estado()
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
