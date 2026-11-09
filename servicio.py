
from abc import ABC, abstractmethod
from excepciones import ErrorServicio, DatosInvalidos


class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        if not nombre or not nombre.strip():
            raise DatosInvalidos("El nombre del servicio es obligatorio.")

        if precio_base <= 0:
            raise DatosInvalidos("El precio debe ser mayor que cero.")

        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass
