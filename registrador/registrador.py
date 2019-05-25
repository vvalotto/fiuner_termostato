"""
Clase para realizar el registro de auditoria y excepciones
"""

from abc import ABCMeta, abstractmethod

class AbsRegistrador:

    @staticmethod
    @abstractmethod
    def registrar_error(registro):
        pass

    @staticmethod
    @abstractmethod
    def auditar_funcion(registro):
        pass
