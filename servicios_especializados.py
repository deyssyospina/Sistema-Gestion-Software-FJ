# Importacion de la clase principal y las excepciones.
from servicio import Servicio
from excepciones import ErrorServicio


# Clase para administrar las reservas de salas.
class ReservaSala(Servicio):

    # Valida la duracion de la reserva.
    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero.")

    # Devuelve la descripcion del servicio.
    def describir_servicio(self):
        return "Reserva de salas por horas."


# Clase para administrar el alquiler de equipos.
class AlquilerEquipo(Servicio):

    # Valida los dias de alquiler.
    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("Los días de alquiler deben ser mayores que cero.")

    # Devuelve la descripcion del servicio.
    def describir_servicio(self):
        return "Alquiler de equipos por días."


# Clase para administrar las asesorias especializadas.
class AsesoriaEspecializada(Servicio):

    # Valida las horas de asesoria.
    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise ErrorServicio("La duración debe ser numérica.")

        if duracion <= 0:
            raise ErrorServicio("Las horas de asesoría deben ser mayores que cero.")

    # Devuelve la descripcion del servicio.
    def describir_servicio(self):
        return "Asesoría especializada por horas."