"""
Prueba del Operador o Controlador del Termostato
"""

import servicios_aplicacion.operador_secuencial


if __name__ == "__main__":
    operador = servicios_aplicacion.operador_secuencial.OperadorSecuencial()
    operador.ejecutar()

