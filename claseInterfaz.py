import abc

class ITesorero(abc.ABC):

    @abc.abstractmethod
    def gastos_sueldo_por_empleado(self, dni):
        pass

class IDirector(abc.ABC):

    @abc.abstractmethod
    def modificar_basico(self, dni, nuevo_basico):
        pass

    @abc.abstractmethod
    def modificar_porcentaje_por_cargo(self, dni, nuevo_porcentaje):
        pass

    @abc.abstractmethod
    def modificar_porcentaje_por_categoría(self, dni, nuevo_porcentaje):
        pass

    @abc.abstractmethod
    def modificar_importe_extra(self, dni, nuevo_importe_extra):
        pass