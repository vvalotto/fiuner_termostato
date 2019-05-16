"""
Clase que representa la bateria que alimenta al dispositivo
"""


class Bateria:

    carga_maxima = 5

    @property
    def nivel_de_carga(self):
        return self._nivel_de_carga

    @property
    def indicador(self):
        return self._indicador

    @nivel_de_carga.setter
    def nivel_de_carga(self, valor):
        if valor <= Bateria.carga_maxima * 0.80:
            self._indicador = "BAJA"
            self._nivel_de_carga = valor
        else:
            self._indicador = "NORMAL"
        self._nivel_de_carga = valor
        return
