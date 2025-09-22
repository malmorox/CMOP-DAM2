# 1. Declara tres variables (nombre, edad, altura) con tu información personal y muéstralas por pantalla en una frase.

nombre = "Marcos"
edad = 20 
altura = 1.80

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {altura} metros")


# 2. Crea una constante PI = 3.1416 y calcula el perímetro de un círculo de radio 5.

PI = 3.14159

radio = 5

perimetro = 2 * PI * radio

print(f"El perimetro de un círculo con radio {radio} es {perimetro}")


# 3. Define una constante IVA = 0.21 y calcula el precio final de un producto cuyo precio base es 100.

IVA = 0.21

precio_base = 100

precio_con_iva = precio_base * (1 + IVA)

print(f"El precio con IVA es {precio_con_iva}")


# 4. Declara dos números enteros y calcula su suma, resta, multiplicación, división y resto.

numero1 = 5
numero2 = 10

def sumar(a, b):
    return a + b

def restar(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print(f"Suma: {sumar(numero1, numero2)}")
print(f"Resta: {restar(numero1, numero2)}")
print(f"Multiplicación: {multiplicar(numero1, numero2)}")
print(f"División: {dividir(numero1, numero2)}")


# 5. Declara dos números reales y calcula la media aritmética.

numero1 = 10.8
numero2 = 23.1

media_aritmetica = (numero1 + numero2) / 2

print(f"La media aritmética de {numero1} y {numero2} es {round(media_aritmetica, 2)}")


# 6. Declara dos cadenas de texto ('Hola' y 'Mundo') y únelas en un solo mensaje con un espacio entre ellas.

cadena1 = "Hola"
cadena2 = "Mundo"

print(f"{cadena1} {cadena2}")


# 7. Declara una variable de cada tipo básico (int, float, str, bool) e imprime su valor y su tipo con type().

variable = 1.85

print(variable)
print(type(variable))


# 8. Pregunta al usuario su nombre con input() y muestra el tipo de la variable que se guarda.

pregunta = input("Introduce tu nombre: ")

print(type(pregunta))


# 9. Crea una serie de valores de diferentes tipos (42, 'Python', 3.14, True) e imprime el tipo de cada uno usando varias líneas de print().

variable1 = 42
variable2 = "Python"
variable3 = 3.14
variable4 = True

print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))


# 10. Declara una variable entera edad = 25. Convierte su valor a cadena y muéstralo en un mensaje.

edad = 25

string_edad = str(edad)

print("Tengo " + string_edad + " años")


# 11. Convierte la cadena '123' en entero y súmale 7.

cadena = "123"

cadena_a_int_mas7 = int(cadena) + 7

print(cadena_a_int_mas7)


# 12. Convierte la cadena '3.1416' en número decimal (float) y multiplícalo por 2. 

cadena = "3.1416"

cadena_a_float_por2 = float(cadena) * 2

print(cadena_a_float_por2)


# 13. Declara una variable booleana mayor_edad = True. Convierte su valor a entero y muéstralo en pantalla.

mayor_edad = True

mayor_edad_entero = int(mayor_edad)

print(mayor_edad_entero)


# 14. Escribe un programa que pida al usuario un número real y lo muestre convertido en entero.

numero_real = 17.81

entero = int(numero_real)

print(entero)


# 15. Pide al usuario su nombre y edad. Muestra el mensaje: Hola "nombre", tienes "edad" años.

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

print(f"Hola {nombre}, tienes {edad} años")


# 16. Pide al usuario dos números y muestra la suma, resta, producto y división de ambos.

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

def sumar(a, b):
    return a + b

def restar(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Suma: " + str(sumar(numero1, numero2)))
print("Resta: " + str(restar(numero1, numero2)))
print("Multiplicación: " + str(multiplicar(numero1, numero2)))
print("División: " + str(dividir(numero1, numero2)))


# 17. Pide al usuario el precio de un producto (número real) y muestra el precio con IVA (21%).

IVA = 0.21

pregunta = float(input("Introduce un número real: "))

precio_con_iva = pregunta * (1 + IVA)

print(round(precio_con_iva, 2))


# 18. Pide al usuario su peso (kg) y altura (m), guárdalos en variables y muestra el cálculo del índice de masa corporal (IMC = peso / altura²).

peso = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura (m): "))

imc = peso / (altura ** 2)

print("El índice de masa corporal es: " + str(round(imc, 2)))


# 19. Pide al usuario un número decimal y muéstralo redondeado a entero. 

decimal = float(input("Introduce un número decimal: "))

redondeado_entero = round(decimal)

print(redondeado_entero)


# 20. Escribe un programa que calcule el área de un rectángulo a partir de la base y la altura introducidas por el usuario.

base = float(input("Introduce la base de tu rectángulo: "))
altura = float(input("Introduce la altura de tu rectángulo: "))

area = base * altura
print("El área del rectángulo es: " + str(round(area, 2)))