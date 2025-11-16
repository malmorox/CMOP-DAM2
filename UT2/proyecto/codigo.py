from persistencia import cargar_datos, guardar_datos


def generar_id():
    data = cargar_datos()
    apuestas = data.get("apuestas", [])

    if not apuestas:
        return 1
    
    ids = [int(a["id"]) for a in apuestas]
    return max(ids) + 1


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
            "ganador_real": None
        }

        data["apuestas"].append(apuesta)
        guardar_datos(data)

        print(f"Apuesta creada con ID: {apuesta['id']}")
        return apuesta["id"]

    except Exception as e:
        print("Ha ocurrido un error inesperado creando la apuesta: ", e)


def mostrar_apuestas():
    data = cargar_datos()

    if not data["apuestas"]:
        print("No hay apuestas registradas.")
        return

    print("\n--- LISTA DE APUESTAS ---")
    for apuesta in data["apuestas"]:
        print(f"ID: {apuesta['id']} | {apuesta['equipo1']} vs {apuesta['equipo2']} | Monto: {apuesta['monto']}€ | Participantes: {len(apuesta['participantes'])}")


def buscar_apuesta(apuesta_id):
    data = cargar_datos()

    for apuesta in data["apuestas"]:
        if apuesta["id"] == apuesta_id:
            return apuesta

    return None


def unirse_apuesta():
    apuesta_id = input("ID de la apuesta: ")
    usuario = input("Tu nombre: ")

    apuesta = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe una apuesta con ese ID")
        return

    print(f"Equipos disponibles: {apuesta['equipo1']} / {apuesta['equipo2']}")
    equipo = input("Elige un equipo: ")

    if equipo not in [apuesta["equipo1"], apuesta["equipo2"]]:
        print("Equipo no válido")
        return

    for participante in apuesta["participantes"]:
        if participante["usuario"] == usuario:
            print("Ya estás dentro de esta apuesta")
            return

    apuesta["participantes"].append({
        "usuario": usuario,
        "equipo": equipo
    })

    data = cargar_datos()
    guardar_datos(data)

    print("Te has unido a la apuesta con éxito")


def cerrar_apuesta():
    apuesta_id = input("ID de la apuesta a cerrar: ")

    apuesta = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe esa apuesta")
        return

    ganador = input("Equipo ganador real: ")

    if ganador not in [apuesta["equipo1"], apuesta["equipo2"]]:
        print("Equipo no válido")
        return

    apuesta["ganador_real"] = ganador

    data = cargar_datos()
    guardar_datos(data)

    print(f"Apuesta cerrada. Ganador: {ganador}")


def resultados():
    apuesta_id = input("ID de apuesta para ver resultados: ")
    apuesta = buscar_apuesta(apuesta_id)

    if not apuesta:
        print("No existe esa apuesta")
        return

    if apuesta["ganador_real"] is None:
        print("La apuesta aún no tiene ganador")
        return

    print("\n---- RESULTADOS ----")
    ganadores = []
    perdedores = []

    for participante in apuesta["participantes"]:
        if participante["equipo"] == apuesta["ganador_real"]:
            ganadores.append(participante["usuario"])
        else:
            perdedores.append(participante["usuario"])

    print("Ganadores:", ganadores)
    print("Perdedores:", perdedores)

    if ganadores:
        print("Monto para cada ganador:", apuesta["monto"])
    else:
        print("No hubo ganadores")


def eliminar_apuesta():
    apuesta_id = input("ID de la apuesta a eliminar: ")

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
    else:
        print("Operación cancelada")


def menu():
    while True:
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
""")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Debes escribir un número.")
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


if __name__ == "__main__":
    try:
        menu()
    finally:
        print("Programa finalizado.")