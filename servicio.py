
from abc import ABC, abstractmethod
from excepciones import DatosInvalidos, ServicioNoDisponible


class Servicio(ABC):

    def __init__(self, nombre, precio_base, disponible=True):

        if not nombre or not nombre.strip():
            raise DatosInvalidos("El nombre del servicio es obligatorio.")

        if precio_base <= 0:
            raise DatosInvalidos("El precio debe ser mayor que cero.")

        if not isinstance(disponible, bool):
            raise DatosInvalidos(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):

        if not isinstance(valor, bool):
            raise DatosInvalidos(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._disponible = valor

    def validar_disponibilidad(self):

        if not self._disponible:
            raise ServicioNoDisponible(
                f"El servicio {self._nombre} no está disponible."
            )

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass
