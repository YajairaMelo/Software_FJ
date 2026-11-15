
"""
SOFTWARE FJ
Sistema Integral de Gestion de Clientes, Servicios y Reservas.
Archivo principal de ejecucion.
"""

from software_fj.entidades import Cliente
from software_fj.servicios import (
    Servicio,
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from software_fj.reservas import Reserva

from software_fj.excepciones import (
    SoftwareFJError,
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaNoPermitidaError,
    ClienteDuplicadoError,
    ProcesamientoError
)

from software_fj.logger_config import (
    registrar_evento,
    registrar_advertencia,
    registrar_error,
    registrar_excepcion
)


# ==================================================
# LISTAS INTERNAS DEL SISTEMA
# ==================================================

clientes = []
servicios = []
reservas = []


# ==================================================
# GESTION DE CLIENTES
# ==================================================

def registrar_cliente(identificador, nombre, correo, telefono):
    """Registra un cliente despues de validar sus datos."""

    try:
        cliente = Cliente(
            identificador,
            nombre,
            correo,
            telefono
        )

    except (ValueError, TypeError) as error:
        raise DatosInvalidosError(
            "No fue posible registrar el cliente."
        ) from error

    if any(c.identificador == identificador for c in clientes):
        raise ClienteDuplicadoError(
            "El identificador del cliente ya existe."
        )

    clientes.append(cliente)
    return cliente


def buscar_cliente(identificador):
    """Busca un cliente por su identificador."""

    try:
        cliente = next(
            c for c in clientes
            if c.identificador == identificador
        )

    except StopIteration as error:
        raise DatosInvalidosError(
            "El cliente solicitado no existe."
        ) from error

    else:
        return cliente


# ==================================================
# GESTION DE SERVICIOS
# ==================================================

def registrar_servicio(servicio):
    """Agrega un servicio a la lista interna."""

    if not isinstance(servicio, Servicio):
        raise TypeError("El objeto no corresponde a un servicio válido.")

    if any(s.nombre == servicio.nombre for s in servicios):
        raise ServicioNoDisponibleError(
            "Ya existe un servicio con ese nombre."
        )

    servicios.append(servicio)
    return servicio


def buscar_servicio(nombre):
    """Busca un servicio por su nombre."""

    try:
        servicio = next(
            s for s in servicios
            if s.nombre == nombre
        )

    except StopIteration as error:
        raise ServicioNoDisponibleError(
            "El servicio solicitado no está disponible."
        ) from error

    else:
        return servicio


# ==================================================
# GESTION DE RESERVAS
# ==================================================

def crear_reserva(identificador, id_cliente, nombre_servicio, duracion):
    """Crea una reserva y la almacena en la lista interna."""

    cliente = buscar_cliente(id_cliente)
    servicio = buscar_servicio(nombre_servicio)

    reserva = Reserva(
        identificador,
        cliente,
        servicio,
        duracion
    )

    reservas.append(reserva)
    return reserva


def procesar_reserva_segura(reserva, impuesto=0, descuento=0):
    """Procesa una reserva y encadena los errores de cálculo."""

    try:
        resultado = reserva.procesar(impuesto, descuento)

    except (ValueError, TypeError, RuntimeError) as error:
        raise ProcesamientoError(
            "Error durante el procesamiento de la reserva."
        ) from error

    else:
        registrar_evento(
            f"Reserva {reserva.identificador} procesada correctamente."
        )
        return resultado


# ==================================================
# EJECUCION CONTROLADA DE OPERACIONES
# ==================================================

def ejecutar_operacion(numero, descripcion, funcion):
    """
    Ejecuta una operacion con manejo de excepciones.

    Demuestra:
    try / except / else / finally.
    """

    print(f"\n{'=' * 55}")
    print(f"OPERACION {numero}: {descripcion}")
    print("=" * 55)

    try:
        resultado = funcion()

    except (SoftwareFJError, ValueError, TypeError, RuntimeError) as error:
        print(f"ERROR CONTROLADO: {error}")
        registrar_excepcion(
            f"Operacion {numero} fallida: {descripcion}"
        )

    else:
        print(f"RESULTADO: {resultado}")
        registrar_evento(
            f"Operacion {numero} exitosa: {descripcion}"
        )

    finally:
        print(f"Finalizacion de operacion {numero}.")
        registrar_evento(
            f"Finalizada operacion {numero}."
        )


# ==================================================
# FUNCIONES DE PRUEBA
# ==================================================

def operacion_1():
    return registrar_cliente(
        "C001", "Ana Perez", "ana@gmail.com", "3001234567"
    ).mostrar_informacion()


def operacion_2():
    return registrar_cliente(
        "C002", "Luis Gomez", "luis@gmail.com", "3101234567"
    ).mostrar_informacion()


def operacion_3():
    return registrar_cliente(
        "C003", "Carlos Ruiz", "correo_invalido", "3201234567"
    ).mostrar_informacion()


def operacion_4():
    sala = ReservaSala("Sala Principal", 50000, 30)
    return registrar_servicio(sala).describir_servicio()


def operacion_5():
    equipo = AlquilerEquipo("Computador", 20000, "Portatil")
    return registrar_servicio(equipo).describir_servicio()


def operacion_6():
    asesoria = AsesoriaEspecializada(
        "Consultoria", 80000, "Sistemas"
    )
    return registrar_servicio(asesoria).describir_servicio()


def operacion_7():
    sala_invalida = ReservaSala(
        "Sala Invalida", 50000, -5
    )
    registrar_servicio(sala_invalida)
    return "Servicio creado."


def operacion_8():
    reserva = crear_reserva(
        "R001", "C001", "Sala Principal", 2
    )

    reserva.confirmar()

    costo = procesar_reserva_segura(
        reserva,
        impuesto=19
    )

    return reserva.mostrar_resumen() + f"\nCosto final: ${costo}"


def operacion_9():
    reserva = crear_reserva(
        "R002", "C002", "Computador", 3
    )

    # Intento incorrecto: no se confirma antes de procesar.
    return procesar_reserva_segura(reserva)


def operacion_10():
    reserva = crear_reserva(
        "R003", "C001", "Consultoria", 1
    )

    return reserva.cancelar()


def operacion_11():
    # Duracion invalida.
    return crear_reserva(
        "R004", "C001", "Sala Principal", 0
    )


def operacion_12():
    # Intento de registrar un cliente duplicado.
    return registrar_cliente(
        "C001", "Ana Perez", "ana@gmail.com", "3001234567"
    )


def operacion_13():
    # Intento de cancelar una reserva ya procesada.
    reserva = next(
        r for r in reservas
        if r.identificador == "R001"
    )

    return reserva.cancelar()


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def main():
    """Ejecuta las pruebas integrales de Software FJ."""

    print("\n")
    print("*" * 55)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("*" * 55)

    registrar_evento("Inicio de ejecucion de Software FJ.")

    operaciones = [
        ("Registro de cliente valido", operacion_1),
        ("Registro de segundo cliente", operacion_2),
        ("Registro de cliente con correo invalido", operacion_3),
        ("Creacion de reserva de sala", operacion_4),
        ("Creacion de alquiler de equipo", operacion_5),
        ("Creacion de asesoria especializada", operacion_6),
        ("Creacion de servicio con capacidad invalida", operacion_7),
        ("Reserva confirmada y procesada", operacion_8),
        ("Intento de procesar reserva pendiente", operacion_9),
        ("Cancelacion de reserva pendiente", operacion_10),
        ("Creacion de reserva con duracion invalida", operacion_11),
        ("Registro de cliente duplicado", operacion_12),
        ("Intento de cancelar reserva procesada", operacion_13)
    ]

    for numero, (descripcion, funcion) in enumerate(
        operaciones, start=1
    ):
        ejecutar_operacion(numero, descripcion, funcion)

    print("\n")
    print("*" * 55)
    print("             RESUMEN DEL SISTEMA")
    print("*" * 55)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")

    print("\nSoftware FJ finalizo sus pruebas.")
    print("Los eventos y errores fueron registrados en logs.")

    registrar_evento("Finalizacion de las pruebas de Software FJ.")


if __name__ == "__main__":
    main()
