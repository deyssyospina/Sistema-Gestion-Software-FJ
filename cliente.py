
from abc import ABC, abstractmethod
import re
from excepciones import ErrorCliente, DatosInvalidos


class Entidad(ABC):
    """Clase abstracta para las entidades del sistema."""

    def __init__(self, identificacion):
        if not identificacion:
            raise DatosInvalidos("La identificación es obligatoria.")

        self._identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(Entidad):
    """Representa un cliente de Software FJ."""

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        if not self.__nombre or not self.__nombre.strip():
            raise ErrorCliente("El nombre es obligatorio.")

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", self.__correo):
            raise ErrorCliente("El correo electrónico no es válido.")

        if not self.__telefono.isdigit() or len(self.__telefono) < 7:
            raise ErrorCliente("El teléfono debe tener al menos 7 dígitos.")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificación: {self._identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
