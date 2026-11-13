
# Geraldine Muñoz Jaramillo
# Deyssy Mariana Ospina
# Freddy Samir Bustos
# Codigo: 213023_102
# Ingenieria en Sistemas
# Autoria propia

# MODIFICACIONES REALIZADAS:
# 1. Separacion de errores controlados e inesperados.
# 2. Registro del tipo de excepcion.
# 3. Aviso de operaciones omitidas.
# 4. Seguimiento de operaciones dependientes.
# 5. Mejora en la presentacion del resumen.
# 6. Se agregaron siete simulaciones invalidas.
# 7. Se organizo la operacion 13.
# 8. Se centralizo el calculo de costos en Servicio.


# Importacion de las clases necesarias.
from cliente import Cliente
from servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


# Listas para almacenar clientes y servicios.
clientes = []
servicios = []


# Funcion para ejecutar y controlar cada operacion.
def ejecutar_operacion(numero, descripcion, accion):

    print(f"\nOPERACION {numero}: {descripcion}")

    try:
        # Ejecuta la accion correspondiente.
        resultado = accion()

        print("Resultado:", resultado)

        # Registra la operacion exitosa.
        registrar_evento(f"Operacion {numero}: {descripcion}")

        return resultado

    # MODIFICACION 1:
    # Se separan los errores controlados del sistema de los errores
    # inesperados, para facilitar su identificacion y manejo.
    except ErrorSistema as error:

        print("Error controlado:", error)

        registrar_error(
            f"Operacion {numero} (ErrorSistema): {error}"
        )

        return None

    # MODIFICACION 2:
    # Se identifica el tipo de excepcion y se registra en el log
    # para facilitar la revision de los errores inesperados.
    except Exception as error:

        print(f"Error inesperado ({type(error).__name__}):", error)

        registrar_error(
            f"Operacion {numero} (inesperado, {type(error).__name__}): {error}"
        )

        return None


# MODIFICACION 3:
# Se crea una funcion para informar cuando una operacion no puede
# ejecutarse por falta de datos o por el fallo de una operacion anterior.

# Funcion para informar cuando una operacion no se puede realizar.
def omitir_operacion(numero, descripcion, motivo):

    print(f"\nOPERACION {numero}: {descripcion}")
    print("Omitida:", motivo)

    registrar_error(
        f"Operacion {numero} omitida: {motivo}"
    )


# Funcion para procesar y confirmar la segunda reserva.
def procesar_y_confirmar_reserva(reserva):

    # Procesa la reserva con valores validos.
    resultado = reserva.procesar(0, 0)

    # Confirma la reserva utilizando el costo guardado.
    confirmacion = reserva.confirmar()

    # Devuelve los resultados de las dos acciones.
    return f"Costo: ${resultado:,.2f}. {confirmacion}"


# Funcion principal del sistema.
def iniciar_sistema():

    print("=" * 45)
    print(" SISTEMA INTEGRAL DE GESTION SOFTWARE FJ")
    print("=" * 45)

    # OPERACION 1: Registro de un cliente valido.
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

    # OPERACION 2: Registro de otro cliente.
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

    # OPERACION 3: Prueba de correo invalido.
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

    # OPERACION 4: Creacion de una reserva de sala.
    sala = ejecutar_operacion(
        4,
        "Creacion de servicio de reserva de sala",
        lambda: ReservaSala("Sala de reuniones", 50000)
    )

    # OPERACION 5: Creacion de alquiler de equipos.
    equipo = ejecutar_operacion(
        5,
        "Creacion de servicio de alquiler de equipos",
        lambda: AlquilerEquipo("Computador portatil", 30000)
    )

    # OPERACION 6: Creacion de asesoria especializada.
    asesoria = ejecutar_operacion(
        6,
        "Creacion de asesoria especializada",
        lambda: AsesoriaEspecializada("Asesoria tecnica", 80000)
    )

    # Guarda los servicios creados correctamente.
    for servicio in [sala, equipo, asesoria]:

        if servicio:
            servicios.append(servicio)

    # OPERACION 7: Prueba de servicio no disponible.
    def probar_servicio_no_disponible():

        servicio_prueba = ReservaSala(
            "Sala fuera de servicio",
            50000
        )

        servicio_prueba.disponible = False

        servicio_prueba.validar_disponibilidad()

    ejecutar_operacion(
        7,
        "Intento de utilizar un servicio no disponible",
        probar_servicio_no_disponible
    )

    # OPERACION 8: Creacion de una reserva valida.
    reserva1 = None

    if cliente1 and sala:

        reserva1 = ejecutar_operacion(
            8,
            "Creacion de reserva de sala",
            lambda: Reserva(cliente1, sala, 2)
        )

    else:

        # MODIFICACION 3:
        # Se informa cuando no se puede crear la reserva por falta
        # del cliente o del servicio necesario.
        omitir_operacion(
            8,
            "Creacion de reserva de sala",
            "Falta el cliente 1 o la sala."
        )

    # OPERACION 9: Calculo del costo con descuento e impuesto.
    if reserva1:

        ejecutar_operacion(
            9,
            "Calculo de costo con descuento e impuesto",
            lambda: reserva1.procesar(10, 19)
        )

    else:

        omitir_operacion(
            9,
            "Calculo de costo con descuento e impuesto",
            "La reserva 1 no existe."
        )

    # OPERACION 10: Confirmacion de la primera reserva.
    if reserva1:

        ejecutar_operacion(
            10,
            "Confirmacion de reserva",
            lambda: reserva1.confirmar()
        )

    else:

        omitir_operacion(
            10,
            "Confirmacion de reserva",
            "La reserva 1 no existe."
        )

    # OPERACION 11: Creacion de reserva de equipos.
    reserva2 = None

    if cliente2 and equipo:

        reserva2 = ejecutar_operacion(
            11,
            "Creacion de reserva de equipos",
            lambda: Reserva(cliente2, equipo, 3)
        )

    else:

        omitir_operacion(
            11,
            "Creacion de reserva de equipos",
            "Falta el cliente 2 o el equipo."
        )

    # OPERACION 12: Prueba de descuento invalido.
    if reserva2:

        ejecutar_operacion(
            12,
            "Procesamiento con descuento invalido",
            lambda: reserva2.procesar(150, 19)
        )

    else:

        omitir_operacion(
            12,
            "Procesamiento con descuento invalido",
            "La reserva 2 no existe."
        )

    # MODIFICACION:
    # Se incorpora el seguimiento de la segunda reserva para controlar
    # su confirmacion y evitar que un error detenga el programa.
    #
    # MEJORA POSTERIOR:
    # Se procesa la reserva con valores validos antes de confirmarla.

    # OPERACION 13: Procesamiento y confirmacion de segunda reserva.
    if reserva2:

        ejecutar_operacion(
            13,
            "Procesamiento y confirmacion de segunda reserva",
            lambda: procesar_y_confirmar_reserva(reserva2)
        )

    else:

        omitir_operacion(
            13,
            "Procesamiento y confirmacion de segunda reserva",
            "La reserva 2 no existe."
        )

    # OPERACION 14: Cancelacion de la primera reserva.
    if reserva1:

        ejecutar_operacion(
            14,
            "Cancelacion de reserva",
            lambda: reserva1.cancelar()
        )

    else:

        omitir_operacion(
            14,
            "Cancelacion de reserva",
            "La reserva 1 no existe."
        )

    # SIMULACIONES INVALIDAS ADICIONALES.

    # OPERACION 15: Prueba de identificacion vacia.
    ejecutar_operacion(
        15,
        "Registro de cliente con identificacion vacia",
        lambda: Cliente(
            "",
            "Andres Ruiz",
            "andres@gmail.com",
            "3001234567"
        )
    )

    # OPERACION 16: Prueba de nombre vacio.
    ejecutar_operacion(
        16,
        "Registro de cliente con nombre vacio",
        lambda: Cliente(
            "1004",
            "",
            "andres@gmail.com",
            "3001234567"
        )
    )

    # OPERACION 17: Prueba de telefono con letras.
    ejecutar_operacion(
        17,
        "Registro de cliente con telefono invalido",
        lambda: Cliente(
            "1005",
            "Laura Perez",
            "laura@gmail.com",
            "300ABC4567"
        )
    )

    # OPERACION 18: Prueba de telefono demasiado corto.
    ejecutar_operacion(
        18,
        "Registro de cliente con telefono corto",
        lambda: Cliente(
            "1006",
            "Andres Gomez",
            "andres2@gmail.com",
            "12345"
        )
    )

    # OPERACION 19: Prueba de nombre de servicio vacio.
    ejecutar_operacion(
        19,
        "Creacion de servicio con nombre vacio",
        lambda: ReservaSala("", 50000)
    )

    # OPERACION 20: Prueba de precio igual a cero.
    ejecutar_operacion(
        20,
        "Creacion de servicio con precio cero",
        lambda: AlquilerEquipo("Equipo de prueba", 0)
    )

    # OPERACION 21: Prueba de duracion igual a cero.
    if cliente1 and sala:

        ejecutar_operacion(
            21,
            "Creacion de reserva con duracion cero",
            lambda: Reserva(cliente1, sala, 0)
        )

    else:

        omitir_operacion(
            21,
            "Creacion de reserva con duracion cero",
            "Falta el cliente 1 o la sala."
        )

    # RESUMEN FINAL DEL SISTEMA.
    print("\n" + "=" * 45)
    print(" RESUMEN DEL SISTEMA")
    print("=" * 45)

    # Muestra la cantidad de elementos registrados.
    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(Reserva.reservas))

    # Muestra la informacion de las reservas.
    for reserva in Reserva.reservas:

        # MODIFICACION 5:
        # Se comprueba que mostrar_reserva() devuelva informacion
        # antes de imprimirla, evitando mostrar el valor None.
        detalle = reserva.mostrar_reserva()

        if detalle is not None:
            print("\n" + str(detalle))

    # Finaliza el programa y registra el cierre.
    print("\nEl sistema finalizo sus operaciones.")
    print("Los eventos y errores se guardaron en el archivo de logs.")

    registrar_evento(
        "Finalizacion de las operaciones del sistema."
    )


# Ejecuta el sistema cuando se inicia este archivo.
if __name__ == "__main__":
    iniciar_sistema()
