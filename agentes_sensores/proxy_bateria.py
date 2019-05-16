"""
Primera version: simula una lectura
"""


class ProxyBateria():

    def leer_carga(self):
        '''
        Aqui lee desde la GPIO el valor que indica la bateria
        :return:
        '''
        archivo = open("bateria", "r")
        carga = float(archivo.read())
        archivo.close()
        return carga
