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

def ej1():
    for alumno in alumnos:
        print(alumno["nombre"])

def ej2():
    for alumno in alumnos:
        print(f'{alumno["nombre"]} tiene {alumno["hijos"]} hijos')

def ej3(nombre):
    encontrado = False
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre.lower():
            print(f'Información de {alumno["nombre"]}:')
            print(f'Hijos: {alumno["hijos"]}')
            print(f'Edad: {alumno["edad"]} años')
            print(f'Coche soñado: {alumno["coche"]}')
            print(f'Nota: {alumno["nota"]}')
            encontrado = True
            break
    if not encontrado:
        print("No se ha encontrado el alumno")

def ej4():
    suma = 0
    for alumno in alumnos:
        suma += alumno["nota"]
    media = suma / len(alumnos)
    print(f'La nota media es: {media}')

def ej5():
    mas_hijos = max(alumnos, key=lambda x: x["hijos"])
    menos_hijos = min(alumnos, key=lambda x: x["hijos"])

    print(f"El compañero con mayor número de hijos es {mas_hijos['nombre']} con {mas_hijos['hijos']} hijos")
    print(f"El compañero con menor número de hijos es {menos_hijos['nombre']} con {menos_hijos['hijos']} hijos")

def ej6(valor):
    alumnos_mayores = []

    for alumno in alumnos:
        if alumno["edad"] > valor:
            alumnos_mayores.append(alumno["nombre"])
    print(f'Alumnos mayores de {valor} años: {", ".join(alumnos_mayores)}')

def ej7(textual):
    alumnos_con_valor = []

    for alumno in alumnos:
        if textual.lower() in alumno["coche"].lower():
            alumnos_con_valor.append(alumno["nombre"])
    print(f'Alumnos cuyo coche soñado contiene "{textual}": {", ".join(alumnos_con_valor)}')

def ej8():
    similitudes = {}
    for alumno in alumnos:
        valor = alumno["edad"]
        
        if valor in similitudes:
            similitudes[valor] += 1
        else:
            similitudes[valor] = 1

    max_valor = max(similitudes, key=similitudes.get)
    print(f'La edad que más se repite es {max_valor} años con {similitudes[max_valor]} veces')

def ej9():
    nueva_lista = []

    for alumno in alumnos:
        nuevo_diccionario = {
            "nombre": alumno["nombre"],
            "coche": alumno["coche"]
        }
        nueva_lista.append(nuevo_diccionario)
    
    for item in nueva_lista:
        print(item)

def ej10():
    nuevo_diccionario = {alumno["nombre"]: alumno for alumno in alumnos}

    print(nuevo_diccionario)

def ej11(campo):
    nota_media_por_edad = sum(alumno["nota"] for alumno in alumnos if alumno["edad"] == campo) / len([alumno for alumno in alumnos if alumno["edad"] == campo])
    print(f"Nota media por edad {campo}: {nota_media_por_edad}")

def ej12():
    nueva_lista_ordenada_edad = 

ej1()
ej2()
ej3("Paz")
ej4()
ej5()
ej6(20)
ej7("GTI")
ej8()
ej9()
ej10()
ej11(19)