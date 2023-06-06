from claseInterfaz import IDirector
from abc import ABC, abstractmethod

class Director(ABC):
    def __init__(self, lista_agentes):
        self.lista_agentes = lista_agentes

    def modificarBasico(self, cuil, nuevoBasico):
        agente = self.lista_agentes.buscar_agente_por_cuil(cuil)
        if agente:
            agente.set_sueldo_basico(nuevoBasico)
            print("Sueldo modificado")
        else:
            print("Agente no encontrado")

    def modificarPorcentajeporcargo(self, cuil, nuevoPorcentaje):
        empleado = self.lista_agentes.getDocente(cuil)
        if empleado:
            empleado.set_porcentaje_por_cargo(nuevoPorcentaje)
            print("Porcentaje por cargo modificado exitosamente.")
        else:
            print(f"Empleado con CUIL {cuil} no fue encontrado o no es un Docente")

    def modificarPorcentajeporcategoría(self, cuil, nuevoPorcentaje):
        empleado = self.lista_agentes.getPersonalApoyo(cuil)
        if empleado:
            empleado.set_porcentaje_por_categoria(nuevoPorcentaje)
            print("Porcentaje por categoría modificado exitosamente.")
        else:
            print(f"Empleado con CUIL {cuil} no encontrado o no pertenece al Tipo de Agente Personal de Apoyo")

    def modificarImporteExtra(self, cuil, nuevoImporteExtra):
        empleado = self.lista_agentes.getDocenteInvestigador(cuil)
        if empleado:
            empleado.set_importe_extra(nuevoImporteExtra)
            print("Importe extra modificado exitosamente.")
        else:
            print(f"Empleado con CUIL {cuil} no encontrado o no pertenece al Tipo de Agente Docente Investigador")