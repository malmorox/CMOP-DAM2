import json
import os

RUTA_DB = "bets.json"

def cargar_datos():
    if not os.path.exists(RUTA_DB):
        return {"apuestas": []}

    with open(RUTA_DB, "r") as f:
        return json.load(f)

def guardar_datos(data):
    with open(RUTA_DB, "w") as f:
        json.dump(data, f, indent=4)