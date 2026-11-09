class ErrorSistema(Exception):
    """Error general del sistema."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con los clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con los servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con las reservas."""
    pass


class DatosInvalidos(ErrorSistema):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Error cuando un servicio no está disponible."""
    pass