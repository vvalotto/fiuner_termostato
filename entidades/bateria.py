"""
Clase que representa la bateria que alimenta al dispositivo
"""


class Bateria:

    @property
    def nivel_de_carga(self):
        return self._nivel_de_carga

    @property
    def indicador(self):
        return self._indicador

    @nivel_de_carga.setter
    def nivel_de_carga(self, valor):
        if valor <= self._carga_maxima * self._umbral_de_carga:
            self._indicador = "BAJA"
            self._nivel_de_carga = valor
        else:
            self._indicador = "NORMAL"
        self._nivel_de_carga = valor
        return

    def __init__(self, carga_maxima, umbral_del_carga):
        self._carga_maxima = carga_maxima
        self._umbral_de_carga = umbral_del_carga
        self._nivel_de_carga = 0
        self._indicador = None
        return
