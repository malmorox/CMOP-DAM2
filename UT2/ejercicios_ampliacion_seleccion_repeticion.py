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

a1 = int(input("Introduce el primer término (a1) de la serie aritmética: "))
d = int(input("Introduce la diferencia (d) de la serie aritmética: "))
n = int(input("Introduce el número de términos (n) a sumar: "))

if n > 0:
    Sn = n / 2 * (2 * a1 + (n - 1) * d)
    print(f"La suma de los primeros {n} términos de la serie aritmética es: {Sn}")
else:
    print("El número de términos (n) debe ser positivo")

# Serie de Fibonacci. Pide un número n y muestra los primeros n términos de la serie de Fibonacci.

numero = int(input("Introduce un número para mostrar los primeros n términos de la serie de Fibonacci: "))

a, b = 0, 1

print("Los primeros", numero, "términos de la serie de Fibonacci son:")
for _ in range(numero):
    print(a, end=" ")
    a, b = b, a + b

# Números perfectos. Un número es perfecto si es igual a la suma de sus divisores (excepto él mismo). Pide un número y determina si es perfecto.

numero = int(input("Introduce un número para determinar si es perfecto: "))

suma_divisores = 0
for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print(f"El número {numero} es perfecto")
else:
    print(f"El número {numero} NO es perfecto")


# Potencias sin usar operador **. Pide una base y un exponente, y calcula la potencia mediante multiplicaciones sucesivas.

base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

potencia = 1
for _ in range(exponente):
    potencia *= base

print(f"{base} elevado a la {exponente} es {potencia}")


# Inversión de número. Pide un número entero y muestra su valor invertido (por ejemplo, 1234 → 4321).

numero = int(input("Introduce un número entero para invertirlo: "))
numero_invertido = int(str(numero)[::-1])
print("El número invertido es: " + {numero_invertido})


# Palíndromo numérico. Determina si un número leído por teclado es palíndromo (se lee igual al derecho y al revés).

numero = input("Introduce un número para comprobar si es palíndromo: ")

if numero == numero[::-1]:
    print(f"El número {numero} es palíndromo")
else:
    print(f"El número {numero} NO es palíndromo")


# Conversión decimal → binario. Pide un número entero positivo y convierte a binario sin usar bin(). (Usar divisiones sucesivas entre 2 y guardar los restos.)

numero = int(input("Introduce un número entero positivo para convertir a binario: "))
binario = ""
n = numero

if n == 0:
    binario = "0"
else:
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2

print(f"El número {numero} en binario es: {binario}")


# Máximo común divisor (MCD). Calcula el MCD de dos números usando el algoritmo de Euclides.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

x, y = a, b
while y != 0:
    x, y = y, x % y

print(f"El MCD de {a} y {b} es: {x}")


# Triángulo de Pascal. Pide un número de filas n y muestra el triángulo de Pascal con bucles anidados.

numero = int(input("Introduce el número de filas del triángulo de Pascal: "))

for i in range(numero):
    num = 1
    print(" "*(numero-i-1), end="")
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()


# Números primos en un rango. Pide dos números a y b y muestra todos los primos entre a y b.

a = int(input("Introduce el límite inferior: "))
b = int(input("Introduce el límite superior: "))

for num in range(a, b+1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num, end=" ")


# Descomposición en factores primos. Pide un número y muestra su descomposición en factores primos.

numero = int(input("Introduce un número para descomponer en factores primos: "))
n = numero
factor = 2
print(f"Factores primos de {numero}: ", end="")
while factor <= n:
    if n % factor == 0:
        print(factor, end=" ")
        n = n // factor
    else:
        factor += 1


# Suma de dígitos repetida. Pide un número y suma sus dígitos repetidamente hasta obtener una sola cifra (número digital).

numero = int(input("Introduce un número para calcular su número digital: "))
n = numero

while n >= 10:
    suma = 0
    for digito in str(n):
        suma += int(digito)
    n = suma
print(f"El número digital de {numero} es: {n}")


# Detectar número Armstrong. Un número de 3 cifras es Armstrong si la suma de sus dígitos elevados al cubo es igual al propio número. (Ejemplo: 153 → 1³ + 5³ + 3³ = 153)

numero = int(input("Introduce un número de 3 cifras para comprobar si es Armstrong: "))
c1 = numero // 100
c2 = (numero // 10) % 10
c3 = numero % 10

if c1**3 + c2**3 + c3**3 == numero:
    print(f"{numero} es un número Armstrong")
else:
    print(f"{numero} NO es un número Armstrong")


# Cifras crecientes. Pide un número y determina si sus cifras están en orden creciente (ejemplo: 1359 ✅, 1324 ❌).

numero = input("Introduce un número para verificar si sus cifras son crecientes: ")
creciente = True

for i in range(len(numero)-1):
    if int(numero[i]) >= int(numero[i+1]):
        creciente = False
        break
    
if creciente:
    print(f"Las cifras de {numero} están en orden creciente")
else:
    print(f"Las cifras de {numero} NO están en orden creciente")


# Números primos gemelos. Muestra todos los pares de números primos menores de 100 que difieren en 2 unidades.

primos = []
for num in range(2, 100):
    es_primo = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

for i in range(len(primos)-1):
    if primos[i+1] - primos[i] == 2:
        print(f"({primos[i]}, {primos[i+1]})")


# Secuencia de Collatz (o conjetura del 3n+1). Pide un número y genera la secuencia hasta llegar a 1: Si es par, se divide entre 2. Si es impar, se multiplica por 3 y se suma 1. (Mostrar la secuencia completa.)

numero = int(input("Introduce un número para generar la secuencia de Collatz: "))
n = numero

print(f"Secuencia de Collatz de {numero}: ", end="")
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)