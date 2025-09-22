'''
REQUISITOS MÍNIMOS

Datos del usuario (input):
    Nombre (str)
    Edad (int)
    Altura en metros (float)
    Ciudad de residencia (str)
Variables y constantes:
    Define una constante EDAD_JUBILACION = 65.
    Calcula cuántos años faltan para jubilarse.
Operaciones y conversiones:
    Convierte la altura a centímetros.
    Convierte la edad a cadena para mostrarla con un texto.
Salida (print):
El programa debe mostrar un resumen en formato estructurado
'''


EDAD_JUBILACION = 65

nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura (m): "))
ciudad = str(input("Introduce tu ciudad de residencia: "))

anos_para_jubilacion = EDAD_JUBILACION - edad

altura_en_centimetros = int(round(altura * 100))
edad_str = str(edad)

print("==============================")
print("      TARJETA INTERACTIVA")
print("==============================")
print(f"Nombre: {nombre}")
print(f"Edad: {edad_str}")
print(f"Altura: {altura_en_centimetros} cm")
print(f"Ciudad: {ciudad}")
print(f"Años hasta la jubilación: {anos_para_jubilacion}")
print("==============================")