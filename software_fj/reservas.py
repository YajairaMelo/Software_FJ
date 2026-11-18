
from software_fj.entidades import Cliente
from software_fj.servicios import Servicio


class Reserva:
    """
    Gestiona las reservas de clientes para los servicios
    ofrecidos por Software FJ.
    """

    ESTADOS_VALIDOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA", "PROCESADA")

    def __init__(self, identificador, cliente, servicio, duracion):
        # Validar identificador
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador de la reserva es obligatorio.")

        # Validar cliente
        if not isinstance(cliente, Cliente):
            raise TypeError("La reserva debe tener un cliente válido.")

        # Validar servicio
        if not isinstance(servicio, Servicio):
            raise TypeError("La reserva debe tener un servicio válido.")

        # Validar duración
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise TypeError("La duración debe ser numérica.")

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self.__identificador = identificador.strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "PENDIENTE"
        self.__costo_total = None

    @property
    def identificador(self):
        return self.__identificador

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo_total(self):
        return self.__costo_total

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "PENDIENTE":
            raise RuntimeError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "CONFIRMADA"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva que todavía no ha sido procesada."""

        if self.__estado not in ("PENDIENTE", "CONFIRMADA"):
            raise RuntimeError(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self.__estado = "CANCELADA"
        return "Reserva cancelada correctamente."

    def procesar(self, impuesto=0, descuento=0):
        """Procesa una reserva confirmada y calcula su costo."""

        if self.__estado != "CONFIRMADA":
            raise RuntimeError(
                "Solo se pueden procesar reservas confirmadas."
            )

        try:
            self.__costo_total = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

        except (ValueError, TypeError) as error:
            raise RuntimeError(
                "No fue posible calcular el costo de la reserva."
            ) from error

        else:
            self.__estado = "PROCESADA"
            return self.__costo_total

    def mostrar_resumen(self):
        """Presenta la información general de la reserva."""

        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {self.__costo_total}"
        )
    
