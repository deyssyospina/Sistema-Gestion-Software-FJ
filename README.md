# SISTEMA INTEGRAL DE GESTIÓN SOFTWARE FJ

## 1. Información del proyecto

**Programa:** Ingeniería en Sistemas  
**Código del grupo:** 213023_102  
**Integrantes:**
- Geraldine Muñoz Jaramillo
- Deyssy Mariana Ospina
- Freddy Samir Bustos

## 2. Descripción del proyecto

El Sistema Integral de Gestión Software FJ es un programa desarrollado en Python que permite administrar clientes, servicios y reservas. Su propósito es facilitar el registro de información, la creación de reservas, el cálculo de costos, la confirmación y la cancelación de reservas.

El sistema también cuenta con validaciones y manejo de excepciones para controlar los errores que pueden presentarse durante su funcionamiento.

## 3. Funcionalidades principales

- Registro y consulta de clientes.
- Creación y administración de servicios.
- Gestión de reservas.
- Cálculo del costo de los servicios.
- Aplicación de descuentos.
- Confirmación y cancelación de reservas.
- Validación de datos ingresados.
- Manejo de excepciones y errores.
- Registro de eventos y errores mediante archivos de log.
- Ejecución y comprobación de 21 operaciones.

## 4. Organización de los archivos

El proyecto está dividido en los siguientes módulos:

| Archivo | Descripción |
|---|---|
| `main.py` | Ejecuta el programa principal y las operaciones. |
| `cliente.py` | Contiene las clases relacionadas con los clientes. |
| `servicio.py` | Administra los servicios y sus costos. |
| `servicios_especializados.py` | Contiene los servicios especializados. |
| `reserva.py` | Gestiona la creación, confirmación y cancelación de reservas. |
| `excepciones.py` | Define las excepciones personalizadas. |
| `logs.py` | Registra los eventos y errores del sistema. |
| `.gitignore` | Evita subir archivos innecesarios al repositorio. |

## 5. Requisitos para ejecutar el programa

- Tener Python instalado.
- Contar con Visual Studio Code o un editor compatible.
- Tener los archivos del proyecto en una misma carpeta.

## 6. Instrucciones de ejecución

1. Descargar o clonar el repositorio desde GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

5. Presionar Enter y verificar los resultados de las operaciones.

## 7. Manejo de errores y registros

El sistema utiliza excepciones personalizadas para controlar situaciones como datos inválidos, errores en las reservas y servicios no disponibles.

También utiliza el módulo de registros para guardar los eventos y errores en el archivo `software_fj.log`, facilitando la revisión del funcionamiento del programa.

## 8. Pruebas realizadas

Se realizaron pruebas para comprobar el funcionamiento del sistema, incluyendo operaciones válidas e inválidas.

Se verificaron 21 operaciones relacionadas con el registro de clientes, creación de servicios, reservas, cálculos de costos, confirmaciones, cancelaciones y manejo de errores.

Entre los resultados comprobados se encuentran:

- **Carlos:** $107.100.
- **María López:** $90.000.

Las pruebas permitieron comprobar las validaciones y el funcionamiento de las diferentes partes del sistema.

## 9. Control de versiones

El proyecto utiliza Git y GitHub para organizar y compartir los cambios realizados por los integrantes del grupo.

Se utiliza el archivo `.gitignore` para evitar subir archivos temporales, carpetas de caché y registros innecesarios.

## 10. Conclusión

El desarrollo de este proyecto permitió aplicar los conocimientos de programación orientada a objetos, manejo de excepciones, validación de datos y control de versiones. Además, se realizaron pruebas para comprobar el funcionamiento de las operaciones y mejorar la organización del sistema.