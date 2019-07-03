from unittest import TestCase
from entidades.ambiente import *
from gestores_entidades.gestor_climatizador import *


class TestGestorClimatizador(TestCase):

    def setUp(self) -> None:
        self._gestor = GestorClimatizador()

    def test_obtener_estado_climatizador_inicializado(self):
        self.assertEqual(self._gestor.obtener_estado_climatizador(), "apagado")

    def test_accionar_climatizador_para_calentar(self):
        self._ambiente = Ambiente()
        self._ambiente.temperatura_ambiente = 20
        self._ambiente.temperatura_deseada = 24
        self._gestor.accionar_climatizador(self._ambiente)
        self.assertEqual(self._gestor.obtener_estado_climatizador(), "calentando")

    def test_accionar_climatizador_calentando(self):
        self._ambiente = Ambiente()
        self._ambiente.temperatura_ambiente = 20
        self._ambiente.temperatura_deseada = 24
        self._gestor.accionar_climatizador(self._ambiente)
        self._ambiente.temperatura_ambiente = 21
        self._gestor.accionar_climatizador(self._ambiente)
        self.assertEqual(self._gestor.obtener_estado_climatizador(), "calentando")

    def test_accionar_climatizador_apaga_porque_calento(self):
        self._ambiente = Ambiente()
        self._ambiente.temperatura_ambiente = 20
        self._ambiente.temperatura_deseada = 24
        self._gestor.accionar_climatizador(self._ambiente)
        self._ambiente.temperatura_ambiente = 23
        self._gestor.accionar_climatizador(self._ambiente)
        self.assertEqual(self._gestor.obtener_estado_climatizador(), "apagado")



