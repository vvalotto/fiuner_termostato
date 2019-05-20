"""
Prueba del Operador o Controlador del Termostato
"""

import servicios_aplicacion.operador_paralelo


if __name__ == "__main__":
    operador = servicios_aplicacion.operador_paralelo.OperadorParalelo()
    operador.ejecutar()

