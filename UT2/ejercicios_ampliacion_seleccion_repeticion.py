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


# Palíndromo numérico. Determina si un número leído por teclado es palíndromo (se lee igual al derecho y al revés).



# Conversión decimal → binario. Pide un número entero positivo y convierte a binario sin usar bin(). (Usar divisiones sucesivas entre 2 y guardar los restos.)



# Máximo común divisor (MCD). Calcula el MCD de dos números usando el algoritmo de Euclides.



# Triángulo de Pascal. Pide un número de filas n y muestra el triángulo de Pascal con bucles anidados.



# Números primos en un rango. Pide dos números a y b y muestra todos los primos entre a y b.



# Descomposición en factores primos. Pide un número y muestra su descomposición en factores primos.



# Suma de dígitos repetida. Pide un número y suma sus dígitos repetidamente hasta obtener una sola cifra (número digital).



# Detectar número Armstrong. Un número de 3 cifras es Armstrong si la suma de sus dígitos elevados al cubo es igual al propio número. (Ejemplo: 153 → 1³ + 5³ + 3³ = 153)



# Cifras crecientes. Pide un número y determina si sus cifras están en orden creciente (ejemplo: 1359 ✅, 1324 ❌).



# Números primos gemelos. Muestra todos los pares de números primos menores de 100 que difieren en 2 unidades.



# Secuencia de Collatz (o conjetura del 3n+1). Pide un número y genera la secuencia hasta llegar a 1: Si es par, se divide entre 2. Si es impar, se multiplica por 3 y se suma 1. (Mostrar la secuencia completa.)