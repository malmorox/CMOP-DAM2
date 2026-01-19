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

# Recorre la lista y muestra solo la clave "nombre" de cada diccionario.
def ej1():
    for alumno in alumnos:
        print(alumno["nombre"])

# Recorre la lista e imprime frases del tipo: "Ana tiene un 7.5"
def ej2():
    for alumno in alumnos:
        print(f'{alumno["nombre"]} tiene {alumno["hijos"]} hijos')

# Pide un nombre al usuario y busca en la lista el diccionario correspondiente.
# Si existe, muestra toda su información. Si no, indica que no se encuentra. 
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

# Calcula la media de una clave numérica de todos los diccionarios de la lista. 
def ej4():
    suma = 0
    for alumno in alumnos:
        suma += alumno["nota"]
    media = suma / len(alumnos)
    print(f'La nota media es: {media}')

# Encuentra el diccionario con el valor más alto, el diccionario con el valor más bajo... Y muestra su nombre y su valor. 
def ej5():
    mas_hijos = max(alumnos, key=lambda x: x["hijos"])
    menos_hijos = min(alumnos, key=lambda x: x["hijos"])

    print(f"El compañero con mayor número de hijos es {mas_hijos['nombre']} con {mas_hijos['hijos']} hijos")
    print(f"El compañero con menor número de hijos es {menos_hijos['nombre']} con {menos_hijos['hijos']} hijos")

# Pide un valor al usuario y devuelve una lista de nombres de quienes superan ese valor. 
def ej6(valor):
    alumnos_mayores = []

    for alumno in alumnos:
        if alumno["edad"] > valor:
            alumnos_mayores.append(alumno["nombre"])
    print(f'Alumnos mayores de {valor} años: {", ".join(alumnos_mayores)}')

# Pide un valor textual y devuelve todos los compañeros que tienen ese valor. Muestra nombre y valor. 
def ej7(textual):
    alumnos_con_valor = []

    for alumno in alumnos:
        if textual.lower() in alumno["coche"].lower():
            alumnos_con_valor.append(alumno["nombre"])
    print(f'Alumnos cuyo coche soñado contiene "{textual}": {", ".join(alumnos_con_valor)}')

# Calcula cuántos alumnos tienen una respuesta común para algún valor. Por ejemplo: {"fútbol": 4, "lectura": 2, "cine": 3, ... }
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

# Genera una nueva lista que contenga solo dos campos a partir de los diccionarios originales. 
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

# Crea un diccionario donde la clave sea el nombre del alumno y el valor sea su diccionario completo. Por ejemplo: { "Ana": {...}, "Luis": {...}, "Marta": {...} }
def ej10():
    nuevo_diccionario = {alumno["nombre"]: alumno for alumno in alumnos}

    print(nuevo_diccionario)

# Calcula, para cada respuesta diferente para un campo, cuál es el valor medio de otro de los campos numéricos. Por ejemplo: Nota media de los alumnos a los que les gusta el fútbol.
def ej11(campo):
    nota_media_por_edad = sum(alumno["nota"] for alumno in alumnos if alumno["edad"] == campo) / len([alumno for alumno in alumnos if alumno["edad"] == campo])
    print(f"Nota media por edad {campo}: {nota_media_por_edad}")

# Crea una nueva lista ordenada de mayor a menor valor. 
def ej12():
    lista_ordenada = sorted(alumnos, key=lambda x: x["nota"], reverse=True)

    for alumno in lista_ordenada:
        print(f'Nombre: {alumno["nombre"]} | Nota: {alumno["nota"]}')

# Ordena la lista por un campo numérico y mostrar, uno a uno, a todos los alumnos. Por ejemplo: "Ana tiene 19 años, Javier tiene 18 años..."
def ej13():
    lista_ordenada = sorted(alumnos, key=lambda x: x["edad"])

    for alumno in lista_ordenada:
        print(f'{alumno["nombre"]} tiene {alumno["edad"]} años')

# Devuelve una lista con todos los alumnos cuyo valor de un campo sea uno concreto. 
def ej14(campo, valor):
    lista_filtrada = [alumno for alumno in alumnos if alumno[campo] == valor]

    for alumno in lista_filtrada:
        print(f'Nombre: {alumno["nombre"]} | {campo.capitalize()}: {alumno[campo]}')

# Pide un nombre y un nuevo valor de un campo y lo modifica en el diccionario correspondiente.
def ej15(nombre, campo, nuevo_valor):
    for alumno in alumnos:
        if alumno["nombre"].lower() == nombre.lower():
            alumno[campo] = nuevo_valor
            print(f'Se ha actualizado el campo {campo} de {nombre} a {nuevo_valor}')
            return
    print("No se ha encontrado el alumno")

# Pide un nombre y elimina su diccionario de la lista. 
def ej16(nombre):
    for i, alumno in enumerate(alumnos):
        if alumno["nombre"].lower() == nombre.lower():
            del alumnos[i]
            print(f'Se ha eliminado a {nombre} de la lista')
            return
    print("No se ha encontrado el alumno")

# Genera un diccionario con: número total de alumnos, media de un campo, máximo de un campo, mínimo de un campo, otro campo textual más común.
def ej17():
    total_alumnos = len(alumnos)
    media_hijos = sum(alumno["hijos"] for alumno in alumnos) / total_alumnos
    max_edad = max(alumno["edad"] for alumno in alumnos)
    min_edad = min(alumno["edad"] for alumno in alumnos)

    edades = [alumno["edad"] for alumno in alumnos]
    edad_mas_comun = max(set(edades), key=edades.count)

    resumen = {
        "total_alumnos": total_alumnos,
        "media_hijos": media_hijos,
        "max_edad": max_edad,
        "min_edad": min_edad,
        "edad_mas_comun": edad_mas_comun
    }

    print(resumen)

# Crea un diccionario del tipo: { "Suspensos": [...], "Aprobados": [...], "Notables": [...], "Sobresalientes": ...] }
#Cada categoría contiene una lista con los nombres correspondientes. 
def ej18():
    categorias = {
        "Suspensos": [],
        "Aprobados": [],
        "Notables": [],
        "Sobresalientes": []
    }

    for alumno in alumnos:
        if alumno["nota"] < 5:
            categorias["Suspensos"].append(alumno["nombre"])
        elif 5 <= alumno["nota"] < 7:
            categorias["Aprobados"].append(alumno["nombre"])
        elif 7 <= alumno["nota"] < 9:
            categorias["Notables"].append(alumno["nombre"])
        else:
            categorias["Sobresalientes"].append(alumno["nombre"])

    print(categorias)

# Por ejemplo: Menores de 18, Entre 18 y 20, Mayores de 20. Devuelve un diccionario con estas listas.
def ej19():
    grupos_edad = {
        "Menores de 18": [],
        "Entre 18 y 20": [],
        "Mayores de 20": []
    }

    for alumno in alumnos:
        if alumno["edad"] < 18:
            grupos_edad["Menores de 18"].append(alumno["nombre"])
        elif 18 <= alumno["edad"] <= 20:
            grupos_edad["Entre 18 y 20"].append(alumno["nombre"])
        else:
            grupos_edad["Mayores de 20"].append(alumno["nombre"])

    print(grupos_edad)

# Crea una nueva lista con los alumnos con un valor numérico superior a un valor determinado. Muestra solo nombre y el valor de ese campo. Por ejemplo: lista de alumnos con nota superior a 8
def ej20(campo, valor):
    lista_filtrada = [alumno for alumno in alumnos if alumno[campo] > valor]

    for alumno in lista_filtrada:
        print(f'Nombre: {alumno["nombre"]} | {campo.capitalize()}: {alumno[campo]}')

# Determina si todos los alumnos tienen un valor superior a un umbral. Devuelve True o False. 
def ej21(campo, umbral):
    resultado = all(alumno[campo] > umbral for alumno in alumnos)
    print(f'Todos los alumnos tienen {campo} superior a {umbral}: {resultado}')

# El usuario debe introducir 5 campos. La función devuelve un diccionario con la misma estructura que los recogidos en clase. de manera simple
def ej22():
    nuevo_alumno = {}
    for _ in range(5):
        clave = input("Introduce el nombre del campo: ")
        valor = input(f"Introduce el valor para {clave}: ")
        try:
            valor = int(valor)
        except ValueError:
            try:
                valor = float(valor)
            except ValueError:
                pass
        nuevo_alumno[clave] = valor
    print("Nuevo alumno añadido:", nuevo_alumno)
    alumnos.append(nuevo_alumno)

# Pide un número N y devuelve los N alumnos con mayor valor en un campo determinado.
def ej23(campo, N):
    lista_ordenada = sorted(alumnos, key=lambda x: x[campo], reverse=True)[:N]

    print(f'Primeros {N} alumnos con mayor número de {campo}')
    for alumno in lista_ordenada:
        print(f'Nombre: {alumno["nombre"]} | {campo.capitalize()}: {alumno[campo]}')

# Por ejemplo: de 16 a 18, de 19 a 21, más de 21. Devuelve un diccionario con la media de nota de cada grupo. 
def ej24():
    grupos = {
        "16-18": [],
        "19-21": [],
        "+21": []
    }

    for alumno in alumnos:
        if 16 <= alumno["edad"] <= 18:
            grupos["16-18"].append(alumno["nota"])
        elif 19 <= alumno["edad"] <= 21:
            grupos["19-21"].append(alumno["nota"])
        else:
            grupos["+21"].append(alumno["nota"])

    medias = {}

    for grupo, notas in grupos.items():
        #if notas:
        #    medias[grupo] = sum(notas) / len(notas)
        #else:
        #    medias[grupo] = 0
        medias[grupo] = sum(notas) / len(notas) if notas else 0

    print(medias)

# Crea un sistema que cuente cuántos valores textuales de un campo contienen una palabra concreta. Por ejemplo: “deporte”, “música”, “arte”.
def ej25(palabra):
    contador = 0
    for alumno in alumnos:
        if palabra.lower() in alumno["coche"].lower():
            contador += 1
    print(f'Numero de alumnos cuyo coche soñado contiene la palabra "{palabra}": {contador}')

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
ej12()
ej13()
ej14("hijos", 1)
ej15("Raúl", "nota", 10.0)
ej16("Aitor")
ej17()
ej18()
ej19()
ej20("nota", 8)
ej21("edad", 18)
#ej22()
ej23("edad", 3)
ej24()
ej25("BMW")