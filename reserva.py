
from excepciones import ErrorReserva, DatosInvalidos
from logs import registrar_evento, registrar_error, registrar_excepcion
from cliente import Cliente
from servicio import Servicio


class Reserva:

    reservas = []

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise DatosInvalidos("Debe ingresar un cliente válido.")

        if not isinstance(servicio, Servicio):
            raise DatosInvalidos("Debe ingresar un servicio válido.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise DatosInvalidos("La duración debe ser numérica.")

        if duracion <= 0:
            raise DatosInvalidos("La duración debe ser mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

        self.__id = len(Reserva.reservas) + 1
        Reserva.reservas.append(self)

        registrar_evento(f"Reserva {self.__id} creada.")

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    @property
    def id(self):
        return self.__id

    def procesar(self, descuento=0, impuesto=0):

        try:
            self.__servicio.validar_parametros(self.__duracion)

            costo = self.__servicio.calcular_costo(
                self.__duracion, descuento, impuesto
            )

        except Exception as error:
            registrar_excepcion("Error al procesar la reserva.")

            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.__costo = costo
            registrar_evento(f"Reserva {self.__id} procesada.")
            return costo

        finally:
            registrar_evento(
                f"Finalizó el intento de procesamiento de la reserva {self.__id}."
            )

    def confirmar(self):

        if self.__costo_total is None:
            self._costo_total=self._servicio.precio*self._horas
            self._estado= "CONFIRMADA"
            retrun f"Reserva confirmada. Total: ${self._costo_total:,.2f}"

        try:
            self.procesar()
            self.__estado = "Confirmada"

        except ErrorReserva:
            registrar_error("No se pudo confirmar la reserva.")
            raise

        else:
            registrar_evento(f"Reserva {self.__id} confirmada.")
            return "Reserva confirmada correctamente."

    def cancelar(self):

        if self.__estado == "Cancelada":
            raise ErrorReserva("La reserva ya está cancelada.")

        self.__estado = "Cancelada"
        registrar_evento(f"Reserva {self.__id} cancelada.")

        return "Reserva cancelada correctamente."

    def mostrar_reserva(self):

        return (
            f"Reserva: {self.__id}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo}"
        )
