# Módulo de catálogo de servicios y cálculo de tarifas - Software FJ

from abc import ABC, abstractmethod
import math


class Servicio(ABC):
    """
    Clase abstracta que establece las características
    generales de los servicios de Software FJ.
    """

    def __init__(self, nombre, tarifa_base):

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre del servicio es obligatorio."
            )

        # Validar tipo de tarifa
        if isinstance(tarifa_base, bool) or not isinstance(
            tarifa_base, (int, float)
        ):
            raise TypeError(
                "La tarifa base debe ser numérica."
            )

        # Validar que la tarifa sea finita
        if not math.isfinite(tarifa_base):
            raise ValueError(
                "La tarifa base debe ser un número finito."
            )

        if tarifa_base <= 0:
            raise ValueError(
                "La tarifa base debe ser mayor que cero."
            )

        # Atributos encapsulados
        self.__nombre = nombre.strip()
        self.__tarifa_base = float(tarifa_base)

    # ==============================================
    # PROPIEDADES
    # ==============================================

    @property
    def nombre(self):
        """Devuelve el nombre del servicio."""
        return self.__nombre

    @property
    def tarifa_base(self):
        """Devuelve la tarifa base numérica del servicio."""
        return self.__tarifa_base

    # ==============================================
    # CALCULO GENERAL DEL COSTO
    # ==============================================

    def _calcular_total(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo total considerando:
- Duración del servicio.
- Impuesto porcentual.
- Descuento porcentual.
        """

        valores = {
            "duración": duracion,
            "impuesto": impuesto,
            "descuento": descuento
        }

        # Validar que todos los valores sean numéricos y finitos
        for nombre, valor in valores.items():

            if isinstance(valor, bool) or not isinstance(
                valor, (int, float)
            ):
                raise TypeError(
                    f"El valor de {nombre} debe ser numérico."
                )

            if not math.isfinite(valor):
                raise ValueError(
                    f"El valor de {nombre} debe ser finito."
                )

        # Validar duración
        if duracion <= 0:
            raise ValueError(
                "La duración debe ser mayor que cero."
            )

        # Validar impuesto
        if not 0 <= impuesto <= 100:
            raise ValueError(
                "El impuesto debe estar entre 0 y 100."
            )

        # Validar descuento
        if not 0 <= descuento <= 100:
            raise ValueError(
                "El descuento debe estar entre 0 y 100."
            )

        # Realizar cálculos
        subtotal = self.__tarifa_base * duracion

        valor_descuento = subtotal * (descuento / 100)

        subtotal_con_descuento = subtotal - valor_descuento

        valor_impuesto = (
            subtotal_con_descuento * (impuesto / 100)
        )

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    # ==============================================
    # METODOS ABSTRACTOS
    # ==============================================

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Devuelve la descripción del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los parámetros específicos del servicio."""
        pass


# ==================================================
# SERVICIO 1: RESERVA DE SALAS
# ==================================================

class ReservaSala(Servicio):
    """Servicio especializado en reserva de salas."""

    def __init__(self, nombre, tarifa_base, capacidad):

        super().__init__(nombre, tarifa_base)

        self.__capacidad = capacidad

        self.validar_parametros()

    @property
    def capacidad(self):
        """Devuelve la capacidad máxima de personas de la sala."""
        return self.__capacidad

    def validar_parametros(self):

        if isinstance(self.__capacidad, bool) or not isinstance(
            self.__capacidad, int
        ):
            raise TypeError(
                "La capacidad debe ser un número entero."
            )

        if self.__capacidad <= 0:
            raise ValueError(
                "La capacidad debe ser mayor que cero."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):

        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad: {self.__capacidad} personas. "
            f"Tarifa base: ${self.tarifa_base:,.2f}."
        )


# ==================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ==================================================

class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, nombre, tarifa_base, tipo_equipo):

        super().__init__(nombre, tarifa_base)

        self.__tipo_equipo = tipo_equipo

        self.validar_parametros()

        self.__tipo_equipo = self.__tipo_equipo.strip()

    @property
    def tipo_equipo(self):
        """Devuelve el tipo de equipo disponible para alquiler."""
        return self.__tipo_equipo

    def validar_parametros(self):

        if not isinstance(self.__tipo_equipo, str):
            raise TypeError(
                "El tipo de equipo debe ser texto."
            )

        if not self.__tipo_equipo.strip():
            raise ValueError(
                "Debe especificar el tipo de equipo."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):

        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Tipo de equipo: {self.__tipo_equipo}. "
            f"Tarifa base: ${self.tarifa_base:,.2f}."
        )


# ==================================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ==================================================

class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesorías."""

    def __init__(self, nombre, tarifa_base, especialidad):

        super().__init__(nombre, tarifa_base)

        self.__especialidad = especialidad

        self.validar_parametros()

        self.__especialidad = self.__especialidad.strip()

    @property
    def especialidad(self):
        """Devuelve el área de especialidad de la asesoría."""
        return self.__especialidad

    def validar_parametros(self):

        if not isinstance(self.__especialidad, str):
            raise TypeError(
                "La especialidad debe ser texto."
            )

        if not self.__especialidad.strip():
            raise ValueError(
                "Debe especificar la especialidad de la asesoría."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        return self._calcular_total(
            duracion, impuesto, descuento
        )

    def describir_servicio(self):

        return (
            f"Asesoría especializada: {self.nombre}. "
            f"Especialidad: {self.__especialidad}. "
            f"Tarifa base: ${self.tarifa_base:,.2f}."
        )
