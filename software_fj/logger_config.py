
import logging
from pathlib import Path


# Identificar la carpeta principal del proyecto.
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Crear la carpeta logs si todavía no existe.
CARPETA_LOGS = RUTA_PROYECTO / "logs"
CARPETA_LOGS.mkdir(parents=True, exist_ok=True)

# Ruta del archivo donde se guardarán los registros.
ARCHIVO_LOG = CARPETA_LOGS / "software_fj.log"


def configurar_logger():
    """
    Configura el sistema de registro de eventos y errores.
    """

    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)

    # Evita agregar manejadores repetidos.
    if not logger.handlers:
        manejador = logging.FileHandler(
            ARCHIVO_LOG,
            encoding="utf-8"
        )

        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        manejador.setFormatter(formato)
        logger.addHandler(manejador)

    return logger


# Crear el logger del proyecto.
logger = configurar_logger()


def registrar_evento(mensaje):
    """Registra un evento informativo."""
    logger.info(mensaje)


def registrar_advertencia(mensaje):
    """Registra una advertencia."""
    logger.warning(mensaje)


def registrar_error(mensaje):
    """Registra un error."""
    logger.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra un error junto con su información técnica."""
    logger.exception(mensaje)
