# Agenda DataFrame Python

Este proyecto es una pequeña agenda de contactos que usa Python, pandas y Tkinter.

## Archivos principales

- `main.py`
  - Punto de entrada de la aplicación.
  - Importa `pintar_pantalla` desde `agenda.agenda` y arranca la interfaz gráfica.

- `agenda/agenda.py`
  - Contiene la lógica de la aplicación y la interfaz Tkinter.
  - Carga los contactos desde `contactos.csv` en un `DataFrame` de pandas.
  - Permite crear, editar, eliminar y listar contactos.
  - Valida los campos del formulario y muestra mensajes de error o confirmación.

- `agenda/__init__.py`
  - Inicializa el paquete `agenda`.
  - Actualmente está vacío, pero permite importar módulos desde `agenda`.

- `contactos.csv`
  - Almacena los datos de la agenda en formato CSV.
  - Es el origen de datos que usa `agenda/agenda.py` para leer y actualizar contactos en memoria.

- `logging.conf`
  - Configura el sistema de logs de Python.
  - Se usa en `agenda/agenda.py` para registrar información de depuración.

- `test_gestion.py`
  - Contiene pruebas unitarias con `unittest`.
  - Está escrito para probar una clase `Agenda` dentro de `agenda.gestion`.
  - Nota: en esta versión actual no existe `agenda/gestion.py`, por lo que las pruebas necesitan ese módulo o una refactorización para ejecutarse correctamente.

- `.gitignore`
  - Lista archivos y carpetas que no deben incluirse en el repositorio.
  - Incluye caches de Python, entornos virtuales, archivos de IDE, logs y bases de datos locales.

## Cómo usar

1. Instala Python 3 y las dependencias necesarias, como `pandas`.
2. Ejecuta `python main.py` para iniciar la aplicación.
3. El programa muestra una ventana gráfica donde puedes gestionar contactos.

## Nota

Este proyecto actúa como una aplicación de escritorio basada en Tkinter que gestiona una lista de contactos usando un `DataFrame` de pandas como estructura de datos.
