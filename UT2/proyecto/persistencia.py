import json
import os

# Defino la ruta del archivo JSON, ya que con 'apuestas.json' a secas no funciona
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DB = os.path.join(BASE_DIR, "apuestas.json")

# Funciones para cargar y guardar datos en formato JSON
def cargar_datos():
    # Si el archivo no existe o está vacio  devuelvo una estructura vacía
    if not os.path.exists(RUTA_DB) or os.path.getsize(RUTA_DB) == 0:
        return {"apuestas": []}

    try:
        with open(RUTA_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"apuestas": []}

def guardar_datos(data):
    with open(RUTA_DB, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)