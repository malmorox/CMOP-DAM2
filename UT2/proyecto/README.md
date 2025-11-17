## 🎰 Apuestas deportivas - Paquete de apuestas en PyPI

Pequeño sistema de apuestas con persistencia de datos en JSON.

Permite:
- Crear apuestas
- Unirse a una apuesta existente
- Cerrar apuestas
- Mostrar resultados
- Eliminar apuestas
- Limpiar toda la base de datos (JSON)

## 📦 Instalación

```bash
pip install apuestas-cli
```

## 🚀 Guía de uso

Puedes importar y usar todas las funciones principales:

```py
from apuestas import (
    crear_apuesta,
    mostrar_apuestas,
    buscar_apuesta,
    unirse_apuesta,
    cerrar_apuesta,
    resultados,
    eliminar_apuesta,
    limpiar_todo,
    menu
)
```

## 🖥️ Ejemplo de uso

Este es un ejemplo de como meter el menú y controlar tú mismo la lógica:

```py
def main():
    while True:
        opcion = menu()

        if opcion is None:
            continue

        if opcion == 1:
            crear_apuesta()
        elif opcion == 2:
            mostrar_apuestas()
        elif opcion == 3:
            unirse_apuesta()
        elif opcion == 4:
            cerrar_apuesta()
        elif opcion == 5:
            resultados()
        elif opcion == 6:
            eliminar_apuesta()
        elif opcion == 7:
            limpiar_todo()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
```

> Nota: El menú no ejecuta nada, solo devuelve la opción marcada.

## 🗄️ Persistencia

El paquete utiliza un archivo JSON (apuestas.json) y un script que gestiona la entrada y salida de datos con:

- `cargar_datos()`
- `guardar_datos()`

No necesitas configurarlo.