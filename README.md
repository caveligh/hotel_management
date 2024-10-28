# Hotel Management System

## Descripción

Este proyecto es un sistema de gestión de reservas de hotel escrito en Python. Su objetivo es proporcionar una forma sencilla y eficiente de gestionar clientes, habitaciones, reservas y pagos, aplicando conceptos de programación modular y asincrónica.

## Estructura del Proyecto

`customers.py`: Maneja la gestión de clientes (agregar, eliminar, listar clientes).

`rooms.py`: Maneja la gestión de habitaciones (agregar, verificar disponibilidad, listar habitaciones).

`reservations.py`: Gestiona las reservas (agregar, cancelar, listar reservas).

`payments.py`: Procesa los pagos de manera asincrónica.`

`utils.py`: Contiene funciones utilitarias, como decorad`ores para validaciones comunes.

`hotel_reservation.py`: Integra todos los módulos anterio`res en un flujo principal de operaciones.

`test_hotel_management.py`: Script para probar todas las f`uncionalidades del sistema.

## Características

- Gestión de clientes (agregar, eliminar, listar).

- Gestión de habitaciones (agregar, verificar disponibilidad, listar).

- Gestión de reservas (crear, cancelar, listar).

- Procesamiento de pagos de manera asincrónica.

- Decoradores para validación de clientes.

## Cómo Ejecutar el Sistema

1. Asegúrate de tener Python 3.8 o superior instalado.

2. Descarga los archivos `hotel_reservation.py` y `test_hotel_management.py`.

3. Abre una terminal o línea de comandos.

4. Navega hasta el directorio donde guardaste los archivos.

5. Para probar la funcionalidad principal, ejecuta el siguiente comando:

  `python hotel_reservation.py`

6. Para ejecutar las pruebas y verificar todas las funcionalidades, ejecuta:

  `python test_hotel_management.py`

### Ejemplo de Uso

**Agregar Cliente**: Permite agregar un cliente con ID, nombre y correo electrónico.

**Hacer una Reserva**: Verifica la disponibilidad de una habitación y, si está disponible, crea una reserva y procesa el pago.

**Cancelar una Reserva**: Cancela una reserva existente y libera la habitación.

## Conceptos Implementados

- Programación Modular: Cada parte del sistema está dividida en módulos para facilitar la comprensión y el mantenimiento.

- Programación Asincrónica: Los pagos se procesan de forma asincrónica para simular operaciones reales y evitar bloqueos.

- Decoradores: Se usa un decorador para validar la existencia de clientes, evitando duplicación de lógica.

## Mejoras Futuras

**Gestión de Fechas Más Compleja**: Incluir validaciones más completas para las fechas de reserva, incluyendo la duración de la estancia.

**Base de Datos**: Persistir los datos de clientes, habitaciones y reservas en una base de datos para que el sistema pueda ser utilizado a gran escala.

**Interfaz de Usuario**: Crear una interfaz gráfica o una API para facilitar la interacción con el sistema.

