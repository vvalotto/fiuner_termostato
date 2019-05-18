"""
Tercera version: refactorizacion:
Se crea un clase abstracta y se derivan sus implementaciones
con las clases concretas que se corresponden
"""
import socket
from abc import ABCMeta, abstractmethod


class AbsProxyBateria(metaclass=ABCMeta):

    @abstractmethod
    def leer_carga(self):
        pass


class ProxyBateriaArchivo(AbsProxyBateria):

    def leer_carga(self):

        archivo = open("bateria", "r")
        carga = float(archivo.read())
        archivo.close()
        return carga


class ProxyBateriaSocket(AbsProxyBateria):

    def leer_carga(self):

        carga = None

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        direccion_servidor = ('localhost', 11000)
        servidor.bind(direccion_servidor)

        servidor.listen(1)
        conexion, direccion_cliente = servidor.accept()

        try:
            while True:
                datos = conexion.recv(4096)
                if not datos:
                    break
                carga = float(datos.decode("utf-8"))
        except ConnectionError("Error en la lectura de la carga"):
            conexion.close()
            print("FIN")

        return carga
