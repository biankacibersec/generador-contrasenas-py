# Generador de Contraseñas Seguras en Python

Este es el proyecto final para la materia de Lógica de Programación.

## Datos
* **Alumno:** Bianka Herbas
* **Materia:** Lógica de Programación
* **Fecha de Entrega:** 18 de octubre de 2025

## Objetivo del Programa
El objetivo de este proyecto es aplicar los fundamentos de la lógica de programación para desarrollar una herramienta de ciberseguridad básica pero esencial, un generador de contraseñas robustas y aleatorias.

## Funcionalidades Principales
El software es una aplicación de consola que:
* Solicita al usuario una **longitud** deseada para la contraseña.
* **Valida** que la longitud sea un número y que esté en un rango seguro (mínimo 8 caracteres).
* Permite al usuario **elegir** si desea incluir letras mayúsculas, números y/o símbolos.
* **Garantiza** que la contraseña generada incluya al menos un carácter de cada tipo seleccionado.
* **Mezcla** aleatoriamente los caracteres para evitar patrones predecibles.

## Integración de Conocimientos de la Materia

Este proyecto integra los conceptos aprendidos a lo largo de las 4 unidades del curso:

### Unidad 1: Resolución de Problemas y Entorno
* **1.3 Pasos para Resolver Problemas:** Se aplicó la metodología completa:
    1.  **Análisis:** Se identificó el problema (contraseñas débiles).
    2.  **Diseño:** Se crearon los diagramas de flujo en Raptor para planificar la solución.
    3.  **Implementación:** Se tradujo la lógica de los diagramas a código Python.
    4.  **Prueba:** Se realizaron pruebas (depuración) para validar la entrada y la salida.
* **2.1 Entorno de Desarrollo:** Se utilizó **VSCode** como el IDE principal para la codificación.
* **2.3 Depuración:** Se usaron sentencias `print()` durante el desarrollo para verificar el valor de las variables (como `caracteresPermitidos` y `contrasena_temporal`) en puntos clave.

### Unidad 3: Condicionales y Bucles
* **1.4 Condicional "IF" y 1.3 Operadores Lógicos:** Los condicionales son la base de este programa.
    * Se usa un `if/elif/else` para validar la longitud de la contraseña.
    * Se usa el operador `and` para crear una condición compuesta (`if longitud >= 8 and longitud <= 64`).
    * Se usan múltiples `if` para agregar caracteres a la lista (`if usar_mayusculas: ...`).
* **2.2 Bucle "While" y "For":**
    * Se usa un bucle `while True:` para validar la entrada del usuario, obligándolo a ingresar un número válido.
    * Se usa un bucle `for _ in range(longitud_restante):` para rellenar la contraseña hasta alcanzar la longitud deseada.

### Unidad 4: Estructura de Datos y Funciones
* **1.2 Listas:** Este proyecto depende de las listas de Python.
    * La variable `caracteres_permitidos` se convierte en una lista.
    * La `contrasena_temporal` se construye como una lista para poder mezclarla (`shuffle`).
    * Se usan métodos de lista como `.append()` y `.extend()`.
* **2.1 Ejecución de Funciones y 2.2 Parámetros:** El código está modularizado usando "programación funcional".
    * Se creó la función `solicitar_opciones()` que no recibe parámetros pero devuelve valores.
    * Se creó la función `generar_contrasena()` que recibe múltiples **parámetros** (longitud, usar_mayusculas, etc.) para poder operar.
