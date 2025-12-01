alumnos = [
    {"nombre": "Alvaro", "hijos": 1, "edad": 19, "coche": "Peugeot", "nota": 4.55},
    {"nombre": "Raúl", "hijos": 0, "edad": 19, "coche": "A-45", "nota": 9.55},
    {"nombre": "Paz", "hijos": 3, "edad": 19, "coche": "308-GTI", "nota": 5.55},
    {"nombre": "Aitor", "hijos": 7, "edad": 19, "coche": "BMWX6", "nota": 8.55},
    {"nombre": "Barroso", "hijos": 1, "edad": 22, "coche": "callen", "nota": 7.55},
    {"nombre": "Fernando", "hijos": 2, "edad": 20, "coche": "RX7", "nota": 3.55},
    {"nombre": "Enrique", "hijos": 4, "edad": 42, "coche": "Mercedes GLB", "nota": 6.55}
]

print("--- ALUMNOS DE CLASE ---")
hijos = []
edades = []

for alumno in alumnos:
    print(f"Nombre: {alumno["nombre"]} | Hijos: {alumno["hijos"]} | Edad: {alumno["edad"]} años | Coche soñado: {alumno["coche"]}")
    #lista_hijos.append(alumno["hijos"])
    #edades.append(alumno["edad"])

edades = [alumno["edad"] for alumno in alumnos]
hijos = [alumno["hijos"] for alumno in alumnos]

print("------------------------")

hijos_media = sum(hijos) / len(alumnos)

print(f"Media en las clases: {hijos_media} hijos")

edad_moda = max(edades, key=edades.count)
veces = edades.count(edad_moda)

print(f"La moda es {edad_moda} años y se repite {veces} veces")

nota_mas_alta = max(alumno["nota"] for alumno in alumnos)
nota_mas_baja = min(alumno["nota"] for alumno in alumnos)
print(f"La nota mas alta es: {nota_mas_alta}")
print(f"La nota mas baja es: {nota_mas_baja}")

def filtrarCampo(campo):
    if campo not in alumnos[0]:
        print("No existe ese campo en alumnos")
        return
    else:
        for alumno in alumnos:
            print(alumno[campo], end=", ")

print(filtrarCampo("nombre"))
print(filtrarCampo("apellidos"))