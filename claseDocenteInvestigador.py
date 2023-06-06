from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Investigador, Docente):
    __categoria=''
    __importe_extra=float
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria, importe_extra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion,  carrera, cargo, catedra)
        self.__categoria = categoria
        self.__importe_extra = importe_extra


    def calcular_sueldo(self):
        porcentaje_antiguedad = self.get_antiguedad() * 0.01 * self.get_sueldo_basico()
        porcentaje_cargo = 0.1 if self.get_cargo() == "simple" else 0.2 if self.get_cargo() == "semiexclusivo" else 0.5
        return (
            self.get_sueldo_basico()
            + porcentaje_antiguedad
            + (porcentaje_cargo * self.get_sueldo_basico())
            + self.__importe_extra
        )

    def __str__(self):
        return f"{super().__str__()}, Datos Docente Investigador: {self.__categoria}, {self.__importe_extra}"
    
    def __gt__(self, otro):
        return super().get_nombre() > otro.get_nombre()
    
    def get_categoria(self):
        return self.__categoria
    
    def get_importe_extra(self):
        return self.__importe_extra
    
    def set_importe_extra(self, dato):
        self.__importe_extra=dato
    
    
    def to_dict(self):
        # Obtener el diccionario de la superclase Investigador
        investigador_dict = super().to_dict()

        # Agregar los atributos propios de la clase DocenteInvestigador
        investigador_dict['categoria'] = self.__categoria
        investigador_dict['importe_extra'] = self.__importe_extra

        return investigador_dict
    
   