"""
Clase que representa el ambiente a climatizar
"""


class Ambiente:

    @property
    def temperatura_ambiente(self):
        return self._temperatura_ambiente

    @temperatura_ambiente.setter
    def temperatura_ambiente(self, valor):
        self._temperatura_ambiente = valor
        return

    @property
    def temperatura_deseada(self):
        return self._temperatura_deseada

    @temperatura_deseada.setter
    def temperatura_deseada(self, valor):
        self._temperatura_deseada = valor
        return

    def __init__(self):
        self._temperatura_ambiente = 0
        self._temperatura_deseada = 0
        return
