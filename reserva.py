# Importacion de clases y funciones necesarias.
from excepciones import ErrorReserva, DatosInvalidos
from logs import registrar_evento, registrar_excepcion
from cliente import Cliente
from servicio import Servicio


# Clase que representa las reservas del sistema.
class Reserva:

    # Lista general donde se guardan las reservas.
    reservas = []

    def __init__(self, cliente, servicio, duracion):

        # Comprueba que se ingrese un cliente valido.
        if not isinstance(cliente, Cliente):
            raise DatosInvalidos("Debe ingresar un cliente válido.")

        # Comprueba que se ingrese un servicio valido.
        if not isinstance(servicio, Servicio):
            raise DatosInvalidos("Debe ingresar un servicio válido.")

        # Comprueba que la duracion sea numerica.
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise DatosInvalidos("La duración debe ser numérica.")

        # Comprueba que la duracion sea mayor que cero.
        if duracion <= 0:
            raise DatosInvalidos("La duración debe ser mayor que cero.")

        # Guarda la informacion de la reserva.
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0
        self.__procesada = False

        # Asigna un identificador a la reserva.
        self.__id = len(Reserva.reservas) + 1

        # Agrega la reserva a la lista general.
        Reserva.reservas.append(self)

        # Registra la creacion de la reserva.
        registrar_evento(f"Reserva {self.__id} creada.")

    # Permite consultar el estado de la reserva.
    @property
    def estado(self):
        return self.__estado

    # Permite consultar el costo de la reserva.
    @property
    def costo(self):
        return self.__costo

    # Permite consultar el identificador.
    @property
    def id(self):
        return self.__id

    # Procesa el costo de una reserva.
    def procesar(self, descuento=0, impuesto=0):

        # Comprueba que la reserva este pendiente.
        if self.__estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden procesar reservas pendientes."
            )

        try:
            # Comprueba que el servicio este disponible.
            self.__servicio.validar_disponibilidad()

            # Calcula el costo utilizando el metodo de Servicio.
            costo = self.__servicio.calcular_costo(
                self.__duracion, descuento, impuesto
            )

        except Exception as error:
            # Registra la excepcion que se produjo.
            registrar_excepcion("Error al procesar la reserva.")

            # Genera un error de reserva conservando el error original.
            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

        else:
            # Guarda el costo cuando el procesamiento es correcto.
            self.__costo = costo
            self.__procesada = True

            # Registra el procesamiento exitoso.
            registrar_evento(f"Reserva {self.__id} procesada.")

            return costo

        finally:
            # Registra el final del intento de procesamiento.
            registrar_evento(
                f"Finalizó el intento de procesamiento de la reserva {self.__id}."
            )

    # Confirma una reserva que fue procesada correctamente.
    def confirmar(self):

        # Comprueba que la reserva este pendiente.
        if self.__estado != "Pendiente":
            raise ErrorReserva(
                "No se puede confirmar una reserva que no está pendiente."
            )

        # Comprueba que la reserva haya sido procesada.
        if not self.__procesada:
            raise ErrorReserva(
                "No se puede confirmar una reserva que no ha sido procesada correctamente."
            )

        # Cambia el estado sin recalcular el costo.
        self.__estado = "Confirmada"

        # Registra la confirmacion.
        registrar_evento(f"Reserva {self.__id} confirmada.")

        return (
            f"Reserva confirmada correctamente. "
            f"Total: ${self.__costo:,.2f}"
        )

    # Cancela una reserva.
    def cancelar(self):

        # Evita cancelar una reserva que ya fue cancelada.
        if self.__estado == "Cancelada":
            raise ErrorReserva("La reserva ya está cancelada.")

        # Actualiza el estado de la reserva.
        self.__estado = "Cancelada"

        # Registra la cancelacion.
        registrar_evento(f"Reserva {self.__id} cancelada.")

        return "Reserva cancelada correctamente."

    # Devuelve la informacion completa de la reserva.
    def mostrar_reserva(self):

        return (
            f"Reserva: {self.__id}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo}"
        )