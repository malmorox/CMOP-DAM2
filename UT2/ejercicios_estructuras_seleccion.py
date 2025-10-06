# Pedir un número y mostrar si es positivo o negativo.

numero = float(input("Introduce un número: "))

if numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")


# Pedir un número y mostrar si es par o impar.

numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


# Pedir la edad y mostrar si la persona es mayor de edad (≥18) o no.

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# Pedir una contraseña y comprobar si coincide con la guardada en una variable.

CONTRASENA_PRIVADA = "constrasena"

contrasena = input("Introduce la contrasena: ")

if contrasena == CONTRASENA_PRIVADA:
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta")


# Pedir una nota numérica y mostrar si el alumno aprueba (≥5) o suspende (<5).

nota = int(input("Introduce una nota (0-10): "))

if nota >= 5:
    print("¡Has aprobado!")
elif nota < 5:
    print("Has suspendido :(")


# Pedir un número y mostrar si es múltiplo de 3

numero = int(input("Introduce un número para validar si es múltiplo de 3: "))

if numero / 3 % 0:
    print(f"El {numero} es multiplo de 3")
else:
    print(f"El {numero} NO es multiplo de 3")


# Pedir dos números y mostrar cuál es mayor (o si son iguales).

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

if numero1 > numero2:
    print(f"El {numero1} es mayor que el {numero2}")
elif numero1 < numero2:
    print(f"El {numero1} es menor que el {numero2}")
else:
    print(f"Son iguales")


# Nota 0–4 → suspenso, 5–6 → aprobado, 7–8 → notable, 9–10 → sobresaliente.

nota = int(input("Introduce una nota (0-10): "))

match nota:
    case 0 | 1 | 2 | 3 | 4: print("Suspenso")
    case 5 | 6: print("Aprobado")
    case 7 | 8: print("Notable")
    case 9 | 10: print("Sobresaliente")
    case _: print("Nota incorrecta")


# Pedir un número del 1 al 7 y mostrar qué día corresponde (1 = lunes…).

numero = int(input("Introduce un número del 1 al 7: "))

match numero:
    case 1: print("Lunes")
    case 2: print("Martes")
    case 3: print("Miércoles")
    case 4: print("Jueves")
    case 5: print("Viernes")
    case 6: print("Sábado")
    case 7: print("Domingo")
    case _: print("Número incorrecto")


# Pedir dos números y una operación (+, -, *, /) y mostrar el resultado.

numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))
operacion = input("Introduce una operación (+, -, *, /): ")

match operacion:
    case "+": print(numero1 + numero2)
    case "-": print(numero1 - numero2)
    case "*": print(numero1 * numero2)
    case "/": 
        if numero2 != 0:
            print(numero1 / numero2)
        else:
            print("No se puede dividir entre 0")
    case _: print("Operación incorrecta")


# Pedir edad y si tiene carnet (True/False) y mostrar si puede conducir.

edad = int(input("Introduce tu edad: "))
tiene_carnet = input("¿Tienes carnet de conducir? (True/False): ") == "True"

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")


# Pedir un número y mostrar si está entre 1 y 100.

numero = int(input("Introduce un número: "))

if 1 <= numero <= 100:
    print(f"El {numero} está entre 1 y 100")
else:
    print(f"El {numero} NO está entre 1 y 100")


# Pedir tres notas y mostrar si el alumno aprueba (media ≥5 y ninguna <3).

nota1 = int(input("Introduce la primera nota: "))
nota2 = int(input("Introduce la segunda nota: "))
nota3 = int(input("Introduce la tercera nota: "))

if nota1 >= 3 and nota2 >= 3 and nota3 >= 3:
    media = (nota1 + nota2 + nota3) / 3
    if media >= 5:
        print("¡Has aprobado!")
    else:
        print("Has suspendido :(")
else:
    print("Has suspendido :(")


# Pedir tres lados y mostrar si el triángulo es equilátero, isósceles o escaleno.

lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")


# Pedir un año y determinar si es bisiesto.

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")


# El usuario elige una opción, el ordenador otra (usar random) y se indica quién gana.

import random

opciones = ["piedra", "papel", "tijeras"]

usuario = input("Elige piedra, papel o tijeras: ").lower()
ordenador = random.choice(opciones)

print(f"El ordenador ha elegido {ordenador}")
if usuario == ordenador:
    print("Empate")
elif (usuario == "piedra" and ordenador == "tijeras") or \
     (usuario == "papel" and ordenador == "piedra") or \
     (usuario == "tijeras" and ordenador == "papel"):
    print("¡Has ganado!")
else:
    print("Ha ganado el ordenador")


# Pide al usuario el precio de un producto y su edad. Si el usuario es menor de 18 años → 10% de descuento. Si es mayor o igual a 65 años → 20% de descuento. En otro caso, no hay descuento. Muestra el precio final.

precio = float(input("Introduce el precio del producto: "))
edad = int(input("Introduce tu edad: "))

descuento = 0.0

if edad < 18:
    descuento = 0.10
elif edad >= 65:
    descuento = 0.20

precio_final = precio * (1 - descuento)

print("El producto sale por: " + precio_final + "€")


# Pide al usuario una temperatura y la unidad (C o F). Si la unidad es C, conviértela a Fahrenheit con la fórmula: F = C * 9/5 + 32. Si la unidad es F, conviértela a Celsius con la fórmula: C = (F - 32) * 5/9. Si la unidad no es válida, mostrar un mensaje de error.

temperatura = float(input("Introduce una temperatura: "))
unidad = input("Introduce la unidad (C o F): ")

temperatura_c = 0.0
temperatura_f = 0.0

if unidad == "F":
    temperatura_c = (temperatura - 32) * 5/9
    print(f"{temperatura} grados Fahrenheit son {round(temperatura_c, 2)} grados Celsius")
elif unidad == "C":
    temperatura_f = temperatura * 9/5 + 32
    print(f"{temperatura} grados Celsius son {round(temperatura_f, 2)} grados Fahrenheit")
else:
    print("Unidad no válida")