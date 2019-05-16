
from servicios_aplicacion.selector_entrada import *
from gestores_entidades.gestor_ambiente import *


if __name__ == "__main__":
    gestor = GestorAmbiente()
    gestor.leer_temperatura_ambiente()
    selector = SelectorEntradaTemperatura(gestor)
    gestor.mostrar_temperatura()
    selector.ejecutar()
