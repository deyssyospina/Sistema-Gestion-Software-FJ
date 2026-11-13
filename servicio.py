# Importacion de herramientas y excepciones.
from abc import ABC, abstractmethod
from excepciones import DatosInvalidos, ServicioNoDisponible


# Clase principal para los servicios del sistema.
class Servicio(ABC):

    def __init__(self, nombre, precio_base, disponible=True):

        # Comprueba que el nombre sea valido.
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidos("El nombre del servicio es obligatorio.")

        # Comprueba que el precio sea numerico.
        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool):
            raise DatosInvalidos("El precio debe ser numérico.")

        # Comprueba que el precio sea mayor que cero.
        if precio_base <= 0:
            raise DatosInvalidos("El precio debe ser mayor que cero.")

        # Comprueba que la disponibilidad sea verdadera o falsa.
        if not isinstance(disponible, bool):
            raise DatosInvalidos("La disponibilidad debe ser verdadera o falsa.")

        # Guarda los datos del servicio.
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

    # Permite consultar el nombre del servicio.
    @property
    def nombre(self):
        return self._nombre

    # Permite consultar el precio base.
    @property
    def precio_base(self):
        return self._precio_base

    # Permite consultar la disponibilidad.
    @property
    def disponible(self):
        return self._disponible

    # Permite modificar la disponibilidad.
    @disponible.setter
    def disponible(self, valor):

        # Comprueba que el valor sea booleano.
        if not isinstance(valor, bool):
            raise DatosInvalidos("La disponibilidad debe ser verdadera o falsa.")

        self._disponible = valor

    # Comprueba si el servicio esta disponible.
    def validar_disponibilidad(self):

        if not self._disponible:
            raise ServicioNoDisponible(
                f"El servicio {self._nombre} no está disponible."
            )

    # Calcula el costo total del servicio.
    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        # Valida la duracion segun el tipo de servicio.
        self.validar_parametros(duracion)

        # Comprueba que el descuento sea numerico.
        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise DatosInvalidos("El descuento debe ser numérico.")

        # Comprueba que el impuesto sea numerico.
        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
            raise DatosInvalidos("El impuesto debe ser numérico.")

        # Comprueba que el descuento este entre cero y cien.
        if not 0 <= descuento <= 100:
            raise DatosInvalidos("El descuento debe estar entre 0 y 100.")

        # Comprueba que el impuesto este entre cero y cien.
        if not 0 <= impuesto <= 100:
            raise DatosInvalidos("El impuesto debe estar entre 0 y 100.")

        # Calcula el subtotal segun el precio y la duracion.
        subtotal = self._precio_base * duracion

        # Aplica el descuento correspondiente.
        subtotal -= subtotal * descuento / 100

        # Aplica el impuesto y devuelve el resultado.
        return round(subtotal * (1 + impuesto / 100), 2)

    # Metodo abstracto para describir cada servicio.
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo abstracto para validar la duracion.
    @abstractmethod
    def validar_parametros(self, duracion):
        pass