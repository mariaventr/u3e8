from claseAgente import Agente

class Investigador(Agente):
    __area_investigacion=''
    __tipo_investigacion=''
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion, carrera='', cargo='', catedra=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__area_investigacion = area_investigacion
        self.__tipo_investigacion = tipo_investigacion

    def calcular_sueldo(self):
        porcentaje_antiguedad = self.get_antiguedad() * 0.01 * self.get_sueldo_basico()
        return self.get_sueldo_basico() + porcentaje_antiguedad

    def __str__(self):
        return f"{super().__str__()}, Datos Investigador: {self.__area_investigacion}, {self.__tipo_investigacion}"
    
    def get_area_investigacion(self):
        return self.__area_investigacion
    
    def get_tipo_investigacion(self):
        return self.__tipo_investigacion
    
    def to_dict(self):
        agente_dict = super().to_dict()

        agente_dict['area_investigacion'] = self.__area_investigacion
        agente_dict['tipo_investigacion'] = self.__tipo_investigacion

        return agente_dict
    
    