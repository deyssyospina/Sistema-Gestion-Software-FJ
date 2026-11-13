# Importacion de clases y herramientas necesarias.
from abc import ABC, abstractmethod
import re
from excepciones import ErrorCliente, DatosInvalidos


# Clase abstracta que representa una entidad del sistema.
class Entidad(ABC):

    def __init__(self, identificacion):
        # Comprueba que la identificacion sea valida.
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise DatosInvalidos("La identificación es obligatoria.")

        # Guarda la identificacion de la entidad.
        self._identificacion = identificacion

    # Metodo abstracto para mostrar informacion.
    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase que representa a los clientes.
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        # Inicializa la identificacion heredada.
        super().__init__(identificacion)

        # Guarda los datos privados del cliente.
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        # Comprueba que los datos sean correctos.
        self.validar_datos()

    # Metodo para validar la informacion del cliente.
    def validar_datos(self):

        # Comprueba que el nombre sea obligatorio.
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ErrorCliente("El nombre es obligatorio.")

        # Comprueba que el correo tenga un formato valido.
        if not isinstance(self.__correo, str) or not re.match(
            r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
            self.__correo
        ):
            raise ErrorCliente("El correo electrónico no es válido.")

        # Comprueba que el telefono tenga solamente numeros.
        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ErrorCliente("El teléfono debe contener solamente dígitos.")

        # Comprueba que el telefono tenga minimo siete digitos.
        if len(self.__telefono) < 7:
            raise ErrorCliente("El teléfono debe tener al menos 7 dígitos.")

    # Propiedad para consultar el nombre.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el correo.
    @property
    def correo(self):
        return self.__correo

    # Propiedad para consultar el telefono.
    @property
    def telefono(self):
        return self.__telefono

    # Metodo para mostrar los datos del cliente.
    def mostrar_informacion(self):
        return (
            f"Identificación: {self._identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )