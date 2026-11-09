
from servicio import Servicio
from excepciones import ErrorServicio, DatosInvalidos


def validar_costos(descuento, impuesto):
    if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
        raise DatosInvalidos("El descuento debe ser numérico.")

    if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
        raise DatosInvalidos("El impuesto debe ser numérico.")

    if not 0 <= descuento <= 100:
        raise DatosInvalidos("El descuento debe estar entre 0 y 100.")

    if not 0 <= impuesto <= 100:
        raise DatosInvalidos("El impuesto debe estar entre 0 y 100.")


class ReservaSala(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        validar_costos(descuento, impuesto)

        subtotal = self._precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal * (1 + impuesto / 100), 2)

    def describir_servicio(self):
        return "Reserva de salas por horas."


class AlquilerEquipo(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("Los días de alquiler deben ser mayores que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        validar_costos(descuento, impuesto)

        subtotal = self._precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal * (1 + impuesto / 100), 2)

    def describir_servicio(self):
        return "Alquiler de equipos por días."


class AsesoriaEspecializada(Servicio):

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("Las horas de asesoría deben ser mayores que cero.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)
        validar_costos(descuento, impuesto)

        subtotal = self._precio_base * duracion
        subtotal -= subtotal * descuento / 100
        return round(subtotal * (1 + impuesto / 100), 2)

    def describir_servicio(self):
        return "Asesoría especializada por horas."
