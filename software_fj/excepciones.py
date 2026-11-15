
"""
Excepciones personalizadas del sistema Software FJ.
"""


class SoftwareFJError(Exception):
    """Excepción base del sistema."""
    pass


class DatosInvalidosError(SoftwareFJError):
    """Se genera cuando los datos proporcionados son incorrectos."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaNoPermitidaError(SoftwareFJError):
    """Se genera cuando una operación sobre una reserva no está permitida."""
    pass


class ClienteDuplicadoError(SoftwareFJError):
    """Se genera cuando se intenta registrar un cliente duplicado."""
    pass


class ProcesamientoError(SoftwareFJError):
    """Se genera cuando ocurre un error al procesar una operación."""
    pass
