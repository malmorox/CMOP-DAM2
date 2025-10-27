# División segura. Pedir dos números e intentar dividirlos.
# Capturar división por cero (ZeroDivisionError).
# Mostrar el resultado si no hay error.


numero1 = int(input("Introduce un número:"))
numero2 = int(input("Introduce otro número:"))

try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error al dividir por 0")
else:
    print(f"El resultado de sumar {numero1} y {numero2} es {resultado}")


# Entrada de enteros.
# Pedir un número entero y capturar el error si el usuario introduce texto (ValueError).

try:
    entero = int(input("Introduce un entero: "))
except ValueError:
    print("Has introducido algo que NO es un entero")


# Calculadora con control de errores. Pedir dos números y una operación (+, -, *, /).
# Usar try/except para evitar errores de división por cero o entrada no numérica.
# Mostrar un mensaje si la operación no es válida.

try:
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    
    operacion = input("Introduce la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2
    else:
        print("Operación no válida.")
except ValueError:
    print("Debes introducir solo números")
except ZeroDivisionError:
    print("Error al dividir por 0")
else:
    print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")


# Número par o impar con validación. Pedir un número entero.
# Si no es válido, capturar el error.
# Mostrar si el número es par o impar.

try:
    numero = int(input("Introduce un número entero: "))
    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")
except ValueError:
    print("Debes introducir un número entero válido")


# Pedir número hasta que sea válido.
# Repetir con while hasta que el usuario introduzca un número entero válido.
# Al final, mostrar el número correcto.

while True:
    numero = input("Introduce un número valido: ")
    try:
        numero_int = int(numero)
        break
    except ValueError:
        print("No es un número entero")
    
print("El número correcto es", numero_int)


# Menú con control de excepciones. Mostrar un menú de opciones (1. Sumar, 2. Restar, 3. Salir).
# Capturar si el usuario introduce una opción no numérica o inválida.
# Ejecutar la opción hasta que elija salir.

while True:
    print("1. Sumar, 2. Restar, 3. Salir")
    opcion = input("Selecciona la opción que quieras: ")

    try:
        opcion = int(opcion)
    except ValueError:
        print("Debes introducir una opción valida")
        continue
    

    if opcion == 1 or opcion == 2:
        numero1 = int(input("Introduce un número: "))
        numero2 = int(input("Introduce otro número: "))

        if opcion == 1:
            suma = numero1 + numero2
            print("El resultado de la suma es:", suma)
        elif opcion == 2:
            if numero1 > numero2:
                resta = numero1 - numero2
            elif numero1 < numero2:
                resta = numero2 - numero1
            print("El resultado de la resta es:", resta)   
    elif opcion == 3:
        break
    else:
        print("Opción invalida. Debe ser 1, 2 o 3")


# Conversor de temperaturas robusto. Pedir al usuario una temperatura y la unidad (C o F).
# Capturar errores de conversión de tipo.
# Validar la unidad con selección (if).
# Repetir hasta que se introduzcan datos válidos.

while True:
    try:
        temperatura = float(input("Introduce la temperatura: "))
    except ValueError:
        print("Debes introducir una temperatura valida")
        continue 
    
    unidad = input("Introduce la unidad (C o F): ").upper()
    if unidad not in ["C", "F"]:
        print("Unidad no válida")
        continue
    else:
        if unidad == "C":
            convertida = (temperatura * 9/5) + 32
            print(f"{temperatura}°C equivalen a {convertida:.2f}°F")
        else:
            convertida = (temperatura - 32) * 5/9
            print(f"{temperatura}°F equivalen a {convertida:.2f}°C")

        break


# Juego del adivinador con errores. Generar un número aleatorio del 1 al 10.
# Pedir al usuario que adivine con un while.
# Capturar error si introduce algo que no sea un número (ValueError).
# Indicar con if si el número introducido es mayor o menor que el secreto.

import random

numero_secreto = random.randint(1, 10)
adivinado = False

print("Generando un número del 1 al 10...")

while not adivinado:
    intento = input("Introduce tu número: ")
    
    try:
        intento = int(intento)
        
        if intento < 1 or intento > 10:
            print("Por favor, introduce un número entre 1 y 10.")
            continue
        
        if intento < numero_secreto:
            print("Más alto, intenta de nuevo")
        elif intento > numero_secreto:
            print("Más bajo, intenta de nuevo")
        else:
            print(f"¡Has adivinado el número! ¡¡{numero_secreto}!!")
            adivinado = True
            
    except ValueError:
        print("Debes introducir un número válido")