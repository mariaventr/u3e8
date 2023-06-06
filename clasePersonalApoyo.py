from claseAgente import Agente

class PersonalApoyo(Agente):
    __categoria=0
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__categoria = categoria

    def calcular_sueldo(self):
        porcentaje_categoría = self.calcular_porcentaje_categoria()
        porcentaje_antiguedad = self.calcular_porcentaje_antiguedad()
        sueldo = self.get_sueldo_basico() + (self.get_sueldo_basico() * porcentaje_antiguedad) + (self.get_sueldo_basico() * porcentaje_categoría)
        return sueldo

    def calcular_porcentaje_categoria(self):
        if self.__categoria >= 1 and self.__categoria <= 10:
            porcentaje= 0.1
        elif self.__categoria >= 11 and self.__categoria <= 20:
            porcentaje= 0.2
        elif self.__categoria >= 21 and self.__categoria <= 22:
            porcentaje= 0.3
        else:
            porcentaje= 0
        return porcentaje
    
    def calcular_porcentaje_antiguedad(self):
        return self.get_antiguedad() * 0.01

    def __str__(self):
        return f"{super().__str__()}, Datos Personal: {self.__categoria}"
    
    def set_porcentaje_por_categoria(self, dato):
        self.__categoria=dato
    
    def get_categoria(self):
        return self.__categoria
    
    def to_dict(self):
        # Obtener el diccionario de la superclase Agente
        agente_dict = super().to_dict()

        # Agregar el atributo propio de la clase PersonalApoyo
        agente_dict['categoria'] = self.__categoria

        return agente_dict
    
    