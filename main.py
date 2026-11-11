#Geraldine Muñoz Jaramillo
#Deyssy Mariana Ospina
#Freddy Samir Bustos
#Código: 213023_102
#Ingenieria en Sistemas
#autoría propia
# MODIFICACIONES REALIZADAS:
# 1. Separación de errores controlados e inesperados.
# 2. Registro del tipo de excepción.
# 3. Aviso de operaciones omitidas.
# 4. Seguimiento de operaciones dependientes.
# 5. Mejora en la presentación del resumen.

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
 
    # MODIFICACION 1: antes ErrorSistema se importaba pero nunca se usaba y todo
    # se capturaba con un solo "except Exception". Ahora se separan los
    # errores propios del sistema (esperados, de validacion) de los
    # errores inesperados, para que el log distinga uno de otro.

    except ErrorSistema as error:
        print("Error controlado:", error)
        registrar_error(f"Operacion {numero} (ErrorSistema): {error}")
        return None
 
    except Exception as error:
        # MODIFICACION 2: se muestra y registra el tipo de excepcion
        # (ej. TypeError, ValueError) para facilitar la depuracion.
        print(f"Error inesperado ({type(error).__name__}):", error)
        registrar_error(
            f"Operacion {numero} (inesperado, {type(error).__name__}): {error}"
        )
        return None
 
 
# MODIFICACION 3: funcion nueva. Antes, si una operacion previa fallaba, las
# dependientes se saltaban en silencio (el "if cliente1 and sala"). Ahora
# queda constancia en pantalla y en el log de que fueron omitidas y por que.
def omitir_operacion(numero, descripcion, motivo):
    print(f"\nOPERACION {numero}: {descripcion}")
    print("Omitida:", motivo)
    registrar_error(f"Operacion {numero} omitida: {motivo}")
 
 
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
 
    # OPERACION 3: Intento de registro con correo invalido (debe fallar)
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
 
    # OPERACION 7: Intento de crear un servicio con precio invalido (debe fallar)
    ejecutar_operacion(
        7,
        "Creacion de servicio con precio incorrecto",
        lambda: ReservaSala("Sala invalida", 0)
    )
 
   
    # OPERACION 8: Intento de reserva de un servicio no disponible
sala_mantenimiento = ReservaSala("Sala en Mantenimiento", 50000)
sala_mantenimiento.disponible = False
ejecutar_operacion(
    8,
    "Intento de reserva con servicio no disponible",
    lambda: Reserva(cliente1, sala_mantenimiento, 2)
)
reserva1 = None
 
if clientes and sala:
reserva1 = ejecutar_operacion(
            9,
            "Creacion de reserva de sala",
            lambda: Reserva(clientes, sala, 2)
        )
else:
        # MODIFICACION 3 (aplicado): se avisa en lugar de omitir en silencio
        omitir_operacion(8, "Creacion de reserva de sala",
                         "falta el cliente 1 o la sala")
 
    # OPERACION 9: Calculo de costo con descuento e impuesto
if reserva1:
        ejecutar_operacion(
            9,
            "Calculo de costo con descuento e impuesto",
            lambda: reserva1.procesar(10, 19)
        )
else:
        omitir_operacion(9, "Calculo de costo con descuento e impuesto",
                         "la reserva 1 no existe")
 
    # OPERACION 10: Confirmacion de reserva
if reserva1:
        ejecutar_operacion(
            10,
            "Confirmacion de reserva",
            lambda: reserva1.confirmar()
        )
else:
        omitir_operacion(10, "Confirmacion de reserva",
                         "la reserva 1 no existe")
 
    # OPERACION 11: Creacion de reserva de equipos
reserva2 = None
 
if clientes and equipo:
        reserva2 = ejecutar_operacion(
            11,
            "Creacion de reserva de equipos",
            lambda: Reserva(clientes, equipo, 3)
        )
else:
        omitir_operacion(11, "Creacion de reserva de equipos",
                         "falta el cliente 2 o el equipo")
 
    # OPERACION 12: Intento de procesamiento con descuento invalido (debe fallar)
if reserva2:
        ejecutar_operacion(
            12,
            "Procesamiento con descuento invalido",
            lambda: reserva2.procesar(150, 19)
        )
else:
        omitir_operacion(12, "Procesamiento con descuento invalido",
                         "la reserva 2 no existe")
 
    # OPERACION 13: Confirmacion de segunda reserva
    # MODIFICACION 4: la reserva 2 no pudo procesarse (operacion 12 fallo a
    # proposito). Se deja la operacion tal cual, pero si confirmar() exige
    # que la reserva este procesada, el error quedara registrado en el log
    # como error controlado y no detendra el programa.
if reserva2:
        ejecutar_operacion(
            13,
            "Confirmacion de segunda reserva",
            lambda: reserva2.confirmar()
        )
else:
        omitir_operacion(13, "Confirmacion de segunda reserva",
                         "la reserva 2 no existe")
 
    # OPERACION 14: Cancelacion de una reserva
if reserva1:
        ejecutar_operacion(
            14,
            "Cancelacion de reserva",
            lambda: reserva1.cancelar()
        )
else:
        omitir_operacion(14, "Cancelacion de reserva",
                         "la reserva 1 no existe")

    # OPERACION 15: Intento de confirmar una reserva que ya no está pendiente
if reserva1:
    ejecutar_operacion(
        15,
        "Intento de confirmar reserva no pendiente",
        lambda: reserva1.confirmar()
    )
    # RESUMEN FINAL
    print("\n" + "=" * 45)
    print(" RESUMEN DEL SISTEMA")
    print("=" * 45)
 
    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(Reserva.reservas))
 
    for reserva in Reserva.reservas:
        # MODIFICACION 5: antes se hacia print("\n", reserva.mostrar_reserva()).
        # Si mostrar_reserva() imprime por dentro y no devuelve nada, eso
        # mostraba "None" en pantalla. Ahora solo se imprime si devuelve texto.
        detalle = reserva.mostrar_reserva()
    if detalle is not None:
            print("\n" + str(detalle))
 
    print("\nEl sistema finalizo sus operaciones.")
    print("Los eventos y errores se guardaron en el archivo de logs.")
 
    registrar_evento("Finalizacion de las operaciones del sistema.")

 
if __name__ == "__main__":
    iniciar_sistema()
