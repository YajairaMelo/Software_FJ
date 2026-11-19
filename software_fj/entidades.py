# Módulo de entidades base y gestión de clientes - Software FJ

from abc import ABC, abstractmethod
import re


# ==================================================
# CLASE ABSTRACTA: ENTIDAD
# ==================================================

class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):

        if isinstance(identificador, bool):
            raise TypeError("El identificador no es válido.")

        if not isinstance(identificador, (str, int)):
            raise TypeError(
                "El identificador debe ser texto o entero."
            )

        if not str(identificador).strip():
            raise ValueError(
                "El identificador no puede estar vacío."
            )

        # Atributo encapsulado
        self.__identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self.__identificador

    @abstractmethod
    def validar(self):
        """Define las validaciones de cada entidad."""
        pass

    @abstractmethod
    def mostrar_informacion(self):
        """Define cómo se presenta cada entidad."""
        pass


# ==================================================
# CLASE CLIENTE
# ==================================================

class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.
    Hereda de Entidad y protege sus datos personales.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        # Validar tipos de datos
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")

        if not isinstance(correo, str):
            raise TypeError("El correo debe ser un texto.")

        if not isinstance(telefono, str):
            raise TypeError("El teléfono debe ser un texto.")

        # Atributos privados: encapsulación
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono.strip()

        # Validar los datos al crear el cliente
        self.validar()

    # ==============================================
    # VALIDACIONES
    # ==============================================

    def validar(self):
        """Comprueba que los datos del cliente sean correctos."""

        # Validar nombre
        if not self.__nombre:
            raise ValueError(
                "El nombre del cliente es obligatorio."
            )

        if not any(letra.isalpha() for letra in self.__nombre):
            raise ValueError(
                "El nombre debe contener al menos una letra."
            )

        # Validar correo electrónico
        patron_correo = (
            r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
        )

        if not re.fullmatch(patron_correo, self.__correo):
            raise ValueError(
                "El correo electrónico no es válido."
            )

        # Validar teléfono
        telefono_limpio = (
            self.__telefono.replace(" ", "").replace("-", "")
        )

        if telefono_limpio.startswith("+"):
            telefono_limpio = telefono_limpio[1:]

        if (
            not telefono_limpio.isdigit()
            or not 7 <= len(telefono_limpio) <= 15
        ):
            raise ValueError(
                "El número de teléfono no es válido."
            )

    # ==============================================
    # PROPIEDADES
    # ==============================================

    @property
    def nombre(self):
        """Devuelve el nombre encapsulado del cliente."""
        return self.__nombre

    @property
    def correo(self):
        """Devuelve el correo electrónico del cliente."""
        return self.__correo

    @property
    def telefono(self):
        """Devuelve el número de teléfono del cliente."""
        return self.__telefono

    # ==============================================
    # INFORMACION DEL CLIENTE
    # ==============================================

    def mostrar_informacion(self):
        """Devuelve la información formateada del cliente."""

        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
