
# SOFTWARE FJ
## Sistema Integral de Gestión de Clientes, Servicios y Reservas

### 1. Descripción del proyecto

Software FJ es una aplicación desarrollada en Python que permite gestionar clientes, servicios y reservas mediante programación orientada a objetos.

El sistema administra la información utilizando objetos y listas internas, sin conexión a motores de bases de datos.

### 2. Objetivo

Desarrollar una aplicación modular, estable y extensible que implemente los principios de:

- Abstracción.
- Herencia.
- Encapsulación.
- Polimorfismo.
- Manejo avanzado de excepciones.
- Registro de eventos y errores.

### 3. Tecnologías utilizadas

- Lenguaje: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones: Git y GitHub.
- Almacenamiento: listas y objetos en memoria.
- Registro de eventos: módulo logging de Python.

### 4. Estructura del proyecto

Software_FJ/
│
├── logs/
│   └── software_fj.log
│
├── software_fj/
│   ├── __init__.py
│   ├── entidades.py
│   ├── excepciones.py
│   ├── logger_config.py
│   ├── reservas.py
│   └── servicios.py
│
├── main.py
└── README.md

### 5. Descripción de los módulos

- entidades.py: contiene la clase abstracta Entidad y la clase Cliente.
- servicios.py: contiene la clase abstracta Servicio y sus tres especializaciones.
- reservas.py: administra la creación, confirmación, cancelación y procesamiento de reservas.
- excepciones.py: define las excepciones personalizadas.
- logger_config.py: configura el registro de eventos y errores.
- main.py: integra los módulos y ejecuta las operaciones del sistema.

### 6. Servicios disponibles

1. Reserva de salas.
2. Alquiler de equipos.
3. Asesorías especializadas.

### 7. Manejo de excepciones

El sistema implementa:

- try/except.
- try/except/else.
- try/except/finally.
- Encadenamiento de excepciones.
- Excepciones personalizadas.

### 8. Registro de eventos

Los eventos y errores se almacenan en:

logs/software_fj.log

Se utilizan los niveles INFO, WARNING y ERROR.

### 9. Ejecución del programa

Requisitos:
- Tener Python instalado.
- Abrir la carpeta principal del proyecto en VS Code.

Comando para ejecutar:

py main.py

Comando para verificar sintaxis:

py -m py_compile main.py

### 10. Pruebas del sistema

El programa principal ejecuta 13 operaciones de prueba que incluyen:

- Registro de clientes válidos e inválidos.
- Creación de servicios.
- Validación de parámetros.
- Creación y procesamiento de reservas.
- Cancelación de reservas.
- Detección de clientes duplicados.
- Manejo de operaciones no permitidas.

### 11. Consideraciones

La información se conserva en memoria durante la ejecución del programa. No se utiliza una base de datos.

El archivo de logs permite conservar un registro de eventos y errores.

### 12. Conclusión

Software FJ integra los principios fundamentales de la programación orientada a objetos mediante una arquitectura modular en Python.

Su estructura permite gestionar clientes, servicios y reservas, controlar errores y mantener la continuidad de ejecución ante operaciones incorrectas.
