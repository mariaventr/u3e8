
class Agente(object):
    __cuil=0
    __apellido=''
    __nombre=''
    __sueldo_basico=0.0
    __antiguedad=0
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad,
                 carrera='', cargo='', catedra='', area_investigacion='', tipo_investigacion=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad

    def calcular_sueldo(self):
        pass

    def set_sueldo_basico(self, nuevoBasico):
        self.__sueldo_basico = nuevoBasico

    def __str__(self):
        return f"Datos Agente: {self.__cuil}, {self.__apellido}, {self.__nombre}, {self.__sueldo_basico}, {self.__antiguedad}"
    
    def get_cuil(self):
        return self.__cuil
    
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get_sueldo_basico(self):
        return self.__sueldo_basico
    
    def get_antiguedad(self):
        return self.__antiguedad

    
    def to_dict(self):
        agente_dict = {
            'cuil': self.__cuil,
            'apellido': self.__apellido,
            'nombre': self.__nombre,
            'sueldo_basico': self.__sueldo_basico,
            'antiguedad': self.__antiguedad
        }
        return agente_dict
    