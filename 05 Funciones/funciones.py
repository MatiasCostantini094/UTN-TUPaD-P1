#Actividad 1
"""
def imprimir_hola_mundo():
    
   # Esta función imprime el mensaje "Hola Mundo!" por pantalla.
    
    print("Hola Mundo!") # Esta es la instrucción que se ejecuta al llamar la función

# --- Programa Principal ---
# Aca es donde se "llama" o "ejecuta" la función .
imprimir_hola_mundo()
"""

#Actividad 2
"""
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa Principal
nombre_ingresado = input("Por favor, ingresa tu nombre: ")
saludo_personalizado = saludar_usuario(nombre_ingresado)
# 3. Imprimir el saludo personalizado
print(saludo_personalizado)
"""

#Actividad 3
"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Programa Principal
# 1. Pedir los datos al usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
apellido_usuario = input("Por favor, ingresa tu apellido: ")
edad_usuario = int(input("Por favor, ingresa tu edad: "))
residencia_usuario = input("Por favor, ingresa tu lugar de residencia: ")

# 2. Llamar a la función informacion_personal con los valores ingresados
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
"""
#Actividad 4
"""
import math # Importamos el módulo math para usar math.pi
def calcular_area_circulo(radio):
    # Fórmula del área: pi * radio^2
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    # Fórmula del perímetro: 2 * pi * radio
    perimetro = 2 * math.pi * radio
    return perimetro

# Programa Principal
try:
    radio_ingresado = float(input("Por favor, ingresa el radio del círculo: "))
    # Validar que el radio sea un número positivo
    if radio_ingresado < 0:
        print("El radio no puede ser un número negativo. Por favor, intenta de nuevo.")
    else:
        # 2. Llamar a ambas funciones con el radio ingresado
        area_calculada = calcular_area_circulo(radio_ingresado)
        perimetro_calculado = calcular_perimetro_circulo(radio_ingresado)

        # 3. Mostrar los resultados
        # Usamos f-strings para formatear la salida a 2 decimales para mayor claridad.
        print(f"\nPara un círculo con radio {radio_ingresado}:")
        print(f"El área es: {area_calculada:.2f}")
        print(f"El perímetro es: {perimetro_calculado:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para el radio.")
    """
#Actividad 5
"""
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
# Programa Principal
# 1. Solicita la cantidad de segundos al usuario
try:
    segundos_ingresados = float(input("Por favor, ingresa la cantidad de segundos: "))

    # 2. Validamos que no sea negativo
    if segundos_ingresados < 0:
        print("La cantidad de segundos no puede ser negativa. Por favor, ingresa un valor positivo.")
    else:
        # 3. Se llama a la funcion
        horas_calculadas = segundos_a_horas(segundos_ingresados)
        #Se imprime el resultado
        print(f"\n{segundos_ingresados} segundos equivalen a {horas_calculadas:.2f} horas.")

except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para los segundos.")
    """
#Actividad 6
"""
def tabla_multiplicar(numero):
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    for i in range(1, 11): #rango 1 a 10.
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("----------------------------")

# --- Programa Principal ---
try:
    numero_ingresado = int(input("Por favor, ingresa un número para ver su tabla de multiplicar: "))
    #Llama a la función 
    tabla_multiplicar(numero_ingresado)

except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero válido.")
"""
#Actividad 7
""""
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None 
    return (suma, resta, multiplicacion, division)
# --- Programa Principal ---
# 1. Solicita los dos números al usuario
try:
    num1 = float(input("Por favor, ingresa el primer número: "))
    num2 = float(input("Por favor, ingresa el segundo número: "))
    # 2. Llama a la función operaciones_basicas
    resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = operaciones_basicas(num1, num2)
    # 3.Resultados
    print(f"\n--- Resultados de las Operaciones Básicas ({num1} y {num2}) ---")
    print(f"Suma:          {resultado_suma}")
    print(f"Resta:         {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")

    if resultado_division is not None:
        print(f"División:      {resultado_division:.2f}") # Formatear división a 2 decimales
    else:
        print("División:      Indefinida (División por cero)")
    print("--------------------------------------------------")

except ValueError:
    print("Entrada inválida. Por favor, asegúrate de ingresar números válidos.")
    """
#Actividad 8 
"""
def calcular_imc(peso, altura):
    if altura <= 0: # La altura no puede ser cero o negativa para calcular el IMC.
        return None
    else:
        imc = peso / (altura ** 2)# Fórmula del IMC: peso / (altura * altura)
        return imc
# Programa Principal
try:
    peso_usuario = float(input("Por favor, ingresa tu peso en kilogramos (ej. 85): "))
    altura_usuario = float(input("Por favor, ingresa tu altura en metros (ej. 1.75): "))
    if peso_usuario <= 0:
        print("El peso debe ser un valor positivo. Intenta de nuevo.")
    elif altura_usuario <= 0:
        print("La altura debe ser un valor positivo. Intenta de nuevo.")
    else:
        # 3. Llamar a la funcion
        imc_calculado = calcular_imc(peso_usuario, altura_usuario)
        # 4. Imprime el resultado
        if imc_calculado is not None:
            print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, asegúrate de ingresar números válidos para peso y altura.")
    """
    #Actividad 9
"""
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Programa Principal
try:
    temp_celsius_str = input("Por favor, ingresa la temperatura en grados Celsius: ")
    temperatura_celsius = float(temp_celsius_str)
    # 2. Llama a la funcion
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    # 3. Imprime el resultado
    print(f"\n{temperatura_celsius:.2f}°C equivalen a {temperatura_fahrenheit:.2f}°F.")

except ValueError:
    print("Entrada inválida. Por favor, ingresa un número válido para la temperatura.")
    """
#Actividad 10
"""
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
# Programa Principal
#Se pide que ingrese los 3 numeros
try:
    num1 = float(input("Por favor, ingresa el primer número: "))
    num2 = float(input("Por favor, ingresa el segundo número: "))
    num3 = float(input("Por favor, ingresa el tercer número: "))
    #Llama a la funcion
    promedio_calculado = calcular_promedio(num1, num2, num3)

    # Imprime el resultado
    print(f"\nEl promedio de {num1}, {num2} y {num3} es: {promedio_calculado:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, asegúrate de ingresar solo números.")
    """