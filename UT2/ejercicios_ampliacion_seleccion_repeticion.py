# Suma de números pares e impares. Pide un número n y calcula por separado la suma de los números pares y de los impares entre 1 y n.

numero = int(input("Introduce un número: "))
print("Calculando la suma de los pares e impares por separado...")

suma_pares = 0
suma_impares = 0

for n in range(1, numero+1):
    if n % 2 == 0:
        suma_pares += n
    else:
        suma_impares +=n
    
print(f"La suma de los pares de {str(numero)} es {str(suma_pares)} y la de los impares es {str(suma_impares)}")


# Números divisibles por 3 y 5. Muestra todos los números del 1 al 100 que sean divisibles por 3 o por 5, pero no por ambos.

for numero in range(1, 101):
    if numero % 3 == 0  or numero % 5 == 0:
        if not (numero % 3 == 0 and numero % 5 == 0):
            print(numero, end=" ")


# Factorial de un número. Pide un número entero positivo y calcula su factorial (n!). (Usar un bucle for o while)

numero = int(input("Introduce un número entero positivo para calcular su facturial: "))

factorial = 1

for n in range(1, numero+1):
    factorial *= n

print(f"El factorial de {numero} es {factorial}")


# Contar de dígitos pares e impares. Pide un número y determina cuántos de sus dígitos son pares y cuántos impares.

numero = input("Introduce un número para contar sus dígitos pares e impares: ")

contador_pares = 0
contador_impares = 0

for digito in numero:
    if int(digito) % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print(f"El número {numero} tiene {contador_pares} dígitos pares y {contador_impares} dígitos impares")


# Suma de una serie aritmética. Calcula la suma de los n primeros términos de una serie aritmética, sabiendo el primer término a1 y la diferencia d. Fórmula: Sn = n/2 * (2*a1 + (n-1)*d). (Pide los datos y verifica que n sea positivo).