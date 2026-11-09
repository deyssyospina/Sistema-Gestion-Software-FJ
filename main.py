
from cliente import Cliente
from servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


clientes = []
servicios = []


def ejecutar_operacion(numero, descripcion, accion):
    print(f"\nOPERACION {numero}: {descripcion}")

    try:
        resultado = accion()
        print("Resultado:", resultado)
        registrar_evento(f"Operacion {numero}: {descripcion}")
        return resultado

    except Exception as error:
        print("Error controlado:", error)
        registrar_error(f"Operacion {numero}: {error}")
        return None


def iniciar_sistema():

    print("=" * 45)
    print(" SISTEMA INTEGRAL DE GESTION SOFTWARE FJ")
    print("=" * 45)

    # OPERACION 1: Registro de un cliente valido
    cliente1 = ejecutar_operacion(
        1,
        "Registro de cliente",
        lambda: Cliente(
            "1001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )
    )

    if cliente1:
        clientes.append(cliente1)

    # OPERACION 2: Registro de otro cliente
    cliente2 = ejecutar_operacion(
        2,
        "Registro de segundo cliente",
        lambda: Cliente(
            "1002",
            "Maria Lopez",
            "maria@gmail.com",
            "3101234567"
        )
    )

    if cliente2:
        clientes.append(cliente2)

    # OPERACION 3: Intento de registro con correo invalido
    ejecutar_operacion(
        3,
        "Registro de cliente con correo invalido",
        lambda: Cliente(
            "1003",
            "Pedro Ruiz",
            "correo_incorrecto",
            "3201234567"
        )
    )

    # OPERACION 4: Creacion de reserva de sala
    sala = ejecutar_operacion(
        4,
        "Creacion de servicio de reserva de sala",
        lambda: ReservaSala("Sala de reuniones", 50000)
    )

    # OPERACION 5: Creacion de alquiler de equipos
    equipo = ejecutar_operacion(
        5,
        "Creacion de servicio de alquiler de equipos",
        lambda: AlquilerEquipo("Computador portatil", 30000)
    )

    # OPERACION 6: Creacion de asesoria especializada
    asesoria = ejecutar_operacion(
        6,
        "Creacion de asesoria especializada",
        lambda: AsesoriaEspecializada("Asesoria tecnica", 80000)
    )

    for servicio in [sala, equipo, asesoria]:
        if servicio:
            servicios.append(servicio)

    # OPERACION 7: Intento de crear un servicio con precio invalido
    ejecutar_operacion(
        7,
        "Creacion de servicio con precio incorrecto",
        lambda: ReservaSala("Sala invalida", 0)
    )

    # OPERACION 8: Creacion de una reserva valida
    reserva1 = None

    if cliente1 and sala:
        reserva1 = ejecutar_operacion(
            8,
            "Creacion de reserva de sala",
            lambda: Reserva(cliente1, sala, 2)
        )

    # OPERACION 9: Calculo de costo con descuento e impuesto
    if reserva1:
        ejecutar_operacion(
            9,
            "Calculo de costo con descuento e impuesto",
            lambda: reserva1.procesar(10, 19)
        )

    # OPERACION 10: Confirmacion de reserva
    if reserva1:
        ejecutar_operacion(
            10,
            "Confirmacion de reserva",
            lambda: reserva1.confirmar()
        )

    # OPERACION 11: Creacion de reserva de equipos
    reserva2 = None

    if cliente2 and equipo:
        reserva2 = ejecutar_operacion(
            11,
            "Creacion de reserva de equipos",
            lambda: Reserva(cliente2, equipo, 3)
        )

    # OPERACION 12: Intento de procesamiento con descuento invalido
    if reserva2:
        ejecutar_operacion(
            12,
            "Procesamiento con descuento invalido",
            lambda: reserva2.procesar(150, 19)
        )

    # OPERACION 13: Confirmacion de segunda reserva
    if reserva2:
        ejecutar_operacion(
            13,
            "Confirmacion de segunda reserva",
            lambda: reserva2.confirmar()
        )

    # OPERACION 14: Cancelacion de una reserva
    if reserva1:
        ejecutar_operacion(
            14,
            "Cancelacion de reserva",
            lambda: reserva1.cancelar()
        )

    # RESUMEN FINAL
    print("\n" + "=" * 45)
    print(" RESUMEN DEL SISTEMA")
    print("=" * 45)

    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(Reserva.reservas))

    for reserva in Reserva.reservas:
        print("\n", reserva.mostrar_reserva())

    print("\nEl sistema finalizo sus operaciones.")
    print("Los eventos y errores se guardaron en el archivo de logs.")

    registrar_evento("Finalizacion de las operaciones del sistema.")


if __name__ == "__main__":
    iniciar_sistema()
