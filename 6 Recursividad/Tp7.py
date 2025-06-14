#Trabajo Practico N7 Recursividad
#Ejercicio 1
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Solicitar al usuario un número entero
num = int(input("Introduce un número entero: "))

# Calcular y mostrar los factoriales de 1 hasta num
for i in range(1, num + 1):
    print(f"Factorial de {i}: {factorial(i)}")
"""
# Ejercicio 2
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario un número entero
num = int(input("Introduce la posición de Fibonacci que deseas ver: "))

# Mostrar la serie completa hasta el número ingresado
print("Serie de Fibonacci:")
for i in range(num + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
"""
#Ejercicio 3
"""
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Solicitar al usuario los valores de base y exponente
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular y mostrar el resultado
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
"""
#Ejercicio 4
"""
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar al usuario un número entero
num = int(input("Introduce un número entero positivo: "))

# Calcular y mostrar el resultado en binario
print(f"El número {num} en binario es: {decimal_a_binario(num)}")
"""
#Ejercicio 5
"""
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#  entrada del usuario
cadena = input("Introduce una palabra sin espacios ni tildes: ").lower()
print(f"¿'{cadena}' es un palíndromo? {es_palindromo(cadena)}")
"""
#Ejercicio 6
"""
def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

#  entrada del usuario
num = int(input("Introduce un número entero positivo: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")
"""
#Ejercicio 7 
"""
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# entrada del usuario
num = int(input("Introduce la cantidad de bloques en el nivel más bajo: "))

print(f"Total de bloques necesarios: {contar_bloques(num)}")
"""
#Ejercicio 8
"""
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# entrada del usuario
num = int(input("Introduce un número entero positivo: "))
d = int(input("Introduce el dígito que deseas contar (0-9): "))

print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}.")
"""