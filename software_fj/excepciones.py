# Módulo de jerarquía de excepciones personalizadas - Software FJ

"""
Excepciones personalizadas del sistema Software FJ.
Define los errores específicos de dominio y validación de negocio.
"""


class SoftwareFJError(Exception):
    """Excepción base del sistema de la cual heredan los errores personalizados."""
    pass


class DatosInvalidosError(SoftwareFJError):
    """Se genera cuando los datos proporcionados son incorrectos o no cumplen el formato."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Se genera cuando un servicio solicitado no está disponible."""
    pass


class ReservaNoPermitidaError(SoftwareFJError):
    """Se genera cuando una operación o cambio de estado sobre una reserva no está permitido."""
    pass


class ClienteDuplicadoError(SoftwareFJError):
    """Se genera cuando se intenta registrar un cliente que ya existe en el sistema."""
    pass


class ProcesamientoError(SoftwareFJError):
    """Se genera cuando ocurre un error interno al procesar una operación o cálculo."""
    pass
