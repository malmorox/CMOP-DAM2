from persistencia import cargar_datos, guardar_datos

# Genera un ID único para cada apuesta
def generar_id():
    data = cargar_datos()
    apuestas = data.get("apuestas", [])

    if not apuestas:
        return 1
    
    ids = [int(a["id"]) for a in apuestas]
    return max(ids) + 1

# Crea una nueva apuesta pidiendo los datos al usuario y la guarda
def crear_apuesta():
    try:
        creador = input("Nombre del creador: ")
        equipo1 = input("Equipo 1 (ej: Lakers): ")
        equipo2 = input("Equipo 2 (ej: Warriors): ")

        monto = input("Monto a apostar: ")

        try:
            monto = float(monto)
        except ValueError:
            print("ERROR! El monto debe ser un número")
            return None

        if monto <= 0:
            print("ERROR! El monto debe ser mayor a 0")
            return None

        data = cargar_datos()

        apuesta = {
            "id": generar_id(),
            "creador": creador,
            "equipo1": equipo1,
            "equipo2": equipo2,
            "monto": monto,
            "participantes": [],
            "ganador": None
        }

        data["apuestas"].append(apuesta)
        guardar_datos(data)

        print(f"Apuesta creada con ID: {apuesta['id']}")
        return apuesta["id"]

    except Exception as e:
        print("Ha ocurrido un error inesperado creando la apuesta: ", e)

# Muestra todas las apuestas registradas
def mostrar_apuestas():
    data = cargar_datos()

    if not data["apuestas"]:
        print("No hay apuestas registradas")
        return

    print("\n--- APUESTAS ABIERTAS ---")
    for apuesta in data["apuestas"]:
        print(f"ID: {apuesta['id']} | {apuesta['equipo1']} vs {apuesta['equipo2']} | Monto: {apuesta['monto']}€ | Participantes: {len(apuesta['participantes'])}")

# Busca una apuesta por su ID y devuelve la apuesta y los datos completos
def buscar_apuesta(apuesta_id: int):
    data = cargar_datos()

    for apuesta in data["apuestas"]:
        if apuesta["id"] == apuesta_id:
            return apuesta, data

    return None, data

# Permite a un usuario unirse a una apuesta existente teniendo el ID de la misma
def unirse_apuesta():
    try:
        apuesta_id = int(input("ID de la apuesta: "))
    except ValueError:
        print("El ID debe ser un número entero")
        return
    
    apuesta, data = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe una apuesta con ese ID")
        return
    
    usuario = input("Tu nombre: ")

    for participante in apuesta["participantes"]:
        if participante["usuario"] == usuario:
            print("Ya estás dentro de esta apuesta")
            return

    print(f"Equipos disponibles: {apuesta['equipo1']} / {apuesta['equipo2']}")
    equipo = input("Elige un equipo: ")

    if equipo not in [apuesta["equipo1"], apuesta["equipo2"]]:
        print("Equipo no válido")
        return

    apuesta["participantes"].append({
        "usuario": usuario,
        "equipo": equipo
    })

    guardar_datos(data)

    print("Te has unido a la apuesta con éxito")

# Cierra una apuesta existente, definiendo el equipo ganador para luego mostrar los resultados
def cerrar_apuesta():
    try:
        apuesta_id = int(input("ID de la apuesta que desea cerrar: "))
    except ValueError:
        print("El ID debe ser un número entero")
        return

    apuesta, data = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe esa apuesta")
        return

    ganador = input("Equipo ganador: ")

    if ganador not in [apuesta["equipo1"], apuesta["equipo2"]]:
        print("Equipo no válido")
        return

    apuesta["ganador"] = ganador

    guardar_datos(data)

    print(f"Apuesta cerrada. Ganador: {ganador}")

# Muestra los resultados de una apuesta cerrada, sino indica que no tiene ganador aún
def resultados():
    try:
        apuesta_id = int(input("ID de apuesta para ver resultados: "))
    except ValueError:
        print("El ID debe ser un número entero")
        return
    
    apuesta, _ = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe esa apuesta")
        return

    if apuesta["ganador"] is None:
        print("La apuesta aún no tiene ganador")
        return

    print("\n---- RESULTADOS ----")
    ganadores = []
    perdedores = []

    for participante in apuesta["participantes"]:
        if participante["equipo"] == apuesta["ganador"]:
            ganadores.append(participante["usuario"])
        else:
            perdedores.append(participante["usuario"])

    print("Ganadores:", ganadores)
    print("Perdedores:", perdedores)

    if ganadores:
        print("Monto para cada ganador:", apuesta["monto"])
    else:
        print("No hubo ganadores")

# Elimina una apuesta por su ID
def eliminar_apuesta():
    apuesta_id = int(input("ID de la apuesta que desea eliminar: "))

    data = cargar_datos()

    for apuesta in data["apuestas"]:
        if apuesta["id"] == apuesta_id:
            data["apuestas"].remove(apuesta)
            guardar_datos(data)
            print("Apuesta eliminada")
            return

    print("No se encontró esa apuesta")


def limpiar_todo():
    respuesta = input("¿Seguro que deseas borrar TODAS las apuestas? (s/n): ").lower()

    if respuesta == "s":
        guardar_datos({"apuestas": []})
        print("Se han eliminado todas las apuestas")
    elif respuesta == "n":
        print("Operación cancelada")
    else:
        print("Respuesta no válida")

# Muestra el menu y devuelve la opción, ya el usuario se encargará de validarla
def menu():
    print("""
---- MENÚ PRINCIPAL ----
1. Crear apuesta
2. Mostrar apuestas
3. Unirse a apuesta
4. Cerrar apuesta
5. Ver resultados
6. Eliminar apuesta
7. Limpiar todo
0. Salir
------------------------
""")

    try:
        opcion = int(input("Selecciona una opción: "))
        return opcion
    except ValueError:
        print("Debes introducir un número")
        return None