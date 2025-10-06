# Mostrar los números del 1 al 10 usando un while.

numero = 1

while (numero <= 10):
    print(numero)
    numero += 1


# Mostrar los números del 1 al 10 usando un for y range().

for numero in range(1, 11):
    print(numero)


# Pedir un número al usuario y mostrar la cuenta atrás hasta 0.

numero = int(input("Introduce un número para hacer una cuenta atrás: "))

while (numero >= 0):
    print(numero)
    numero -= 1


# Mostrar los números pares del 1 al 20.

for numero in range(2, 21):
    if numero % 2 == 0:
        print(numero)


# Calcular y mostrar la suma de los números del 1 al 10

suma = 0

for numero in range(1, 11):
    suma += numero

print("La suma es:", suma)


# Pedir un número y mostrar su tabla de multiplicar del 1 al 10.

numero = int(input("Introduce un número para mostrar su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Pedir al usuario números hasta que introduzca un 0, y mostrar la suma total.

suma = 0
numero = -1

while (numero != 0):
    numero = int(input("Introduce un número (0 para salir): "))
    suma += numero

print("La suma total es:", suma)


# Dada la lista ["manzana", "pera", "uva"], mostrar cada elemento.

lista = ["manzana", "pera", "uva"]

for fruta in lista:
    print(fruta)


# Pedir al usuario una palabra y mostrar cada letra en una línea.

palabra = input("Introduce una palabra: ")

for letra in palabra:
    print(letra)


# Pedir una palabra y contar cuántas letras tiene usando un bucle.

palabra = input("Introduce una palabra: ")

contador = 0

for letra in palabra:
    contador += 1

print("La palabra tiene", contador, "letras.")


# Mostrar los impares entre 1 y 50 usando continue.

for numero in range(1, 51):
    if numero % 2 == 0:
        continue
    print(numero)


# Pedir números al usuario hasta que introduzca uno que sea múltiplo de 7.

while True:
    numero = int(input("Introduce un número: "))
    if numero % 7 == 0:
        print("Has introducido un múltiplo de 7")
        break


# El ordenador tiene un número secreto (ej. 15) y el usuario debe adivinarlo.

numero_secreto = 15

numero_usuario = 0

while (numero_usuario != numero_secreto):
    numero_usuario = int(input("Adivina el número secreto: "))

    if numero_usuario < numero_secreto:
        print("El número es mayor")
    elif numero_usuario > numero_secreto:
        print("El número es menor")
    else:
        print("Has ganado")


# Repetir un menú con opciones (1. Saludar, 2. Despedir, 3. Salir) hasta que el usuario elija salir.

opcion = 0

while (opcion != 3):
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Adiós")
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("No válido")


# Pedir notas hasta que el usuario introduzca -1. Mostrar la media de todas.

suma_notas = 0
contador_notas = 0

nota = 0

while (nota != -1):
    nota = int(input("Introduce una nota (-1 para mostrar la media): "))

    if nota != -1:
        suma_notas += nota
        contador_notas += 1
        media = suma_notas / contador_notas
    else:
        if contador_notas > 0:
            print("La media es: ", media)
        else:
            print("No se han introducido notas")


# Pedir un número n y mostrar los n primeros números de la serie de Fibonacci.

numero = int(input("Introduce un número para mostrar su serie de Fibonacci: "))

numero1 = 0
numero2 = 1

for _ in range(numero):
    print(str(numero1), end=" ")
    numero1, numero2 = numero2, numero1+numero2    


# Pedir un número y mostrar si es primo comprobando sus divisores con un bucle.

numero = int(input("Introduce un número para comprobar si es primo: "))

es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
        else:
            es_primo = True
            continue

if es_primo:
    print(f"El {numero} es primo")
else:
    print(f"El {numero} NO es primo")


# Simular un login de usuario - contraseña con 3 posibles intentos.

usuario = "admin"
contrasena = "1234"

intentos = 0

while intentos < 3:
    user = input("Introduce tu usuario: ")
    psw = input("Introduce tu contraseña: ")

    if user == usuario and psw == contrasena:
        print("Login exitoso")
        break
    else:
        print("Login fallido")
        intentos += 1

if intentos == 3:
    print("Has agotado tus intentos")