# Actividad 1-
# Solicita la edad del usuario-
#edad = int(input("Por favor, ingrese su edad: "))
#Verifica si es mayor de edad
#if edad < 0: #validacion que sea mayor que 0
#    print("No es una edad valida.")
#elif edad > 18 and edad < 120: # se establece los parametros para la mayoria de edad
#    print("Es mayor de edad.")
#else:
#    print("No es una edad valida.")

#-Actividad 2-
# Solicita la nota al usuario 
#nota = float(input("Por favor, ingrese su nota: "))

# Verifica si está aprobado o desaprobado
#if nota >= 6:
#   print("Aprobado")
#else:
#   print("Desaprobado")

#- Actividad 3-
# Solicitar un número al usuario
#numero = int(input("Ingrese un número: "))

# Evalua si el número es par utilizando el operador de módulo (%)
#if numero % 2 == 0:
#    print("Ha ingresado un número par.")
#else:
#    print("Por favor, ingrese un número par.")

#- Actividad 4-
# Categoria de edad
#edad = int(input("Ingrese su edad: "))
#if edad < 0: # validacion de edad mayor a 0
#    print("La edad no puede ser negativa.")
#elif edad < 12:
#    print("Eres un niño.")
#elif edad < 18 and edad >= 12:
#    print("Eres un adolescente.")
#elif edad < 30 and edad >= 18:
#    print("Eres un adulto joven.")
#elif edad > 30 and edad <= 120: # validacion de eda no superior a 120
#    print("Eres un adulto mayor.")
#else:
#    print("No es una edad valida.")

#-Activdad 5-
#Ingresar contraseña entre 8 y 14 caracteres
#contraseña = input("Por favor , ingrese una contraseña ")
#Se verifica la longitud de la contraseña
#if 8 <= len(contraseña) <= 14:
#    print("Ha ingresado una contraseña correcta.")
#else:
#    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")

#-Actividad 6-
#lista de numeros aleatorios 
#import random
#from statistics import mode, median, mean
#Lista aleatoria de 50 numeros entre 1 y 100
#numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#Ahora se calcula mode , mediam , mean
#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#moda = mode(numeros_aleatorios)
#tipo de sesgo
#if  media > mediana > moda: 
#    sesgo ="Positivo ( a la derecha)"
#elif media < mediana < moda:
#    sesgo ="Negativo (a la izquierda)"
#else:
#    sesgo = "No hay sesgo"
#Impresion de resultados
#print(f"Numeros aleatorios: {numeros_aleatorios}")
#print(f"Media: {media}")
#print(f"Mediana: {mediana}")
#print(f"Moda: {moda}")
#print(f"Sesgo: {sesgo} ")

#Actividad -8-
#Nombre en mayuscula/minuscula/
#Se solicita el nombre del usuario 
#nombre = input("Por favor , ingresa tu nombre ")
#Opciones para el usuario
#print("Selecciona una opcion :")
#print("1. Mostrar el nombre en mayusculas")
#print("2. Mostrar el nombre en minuscula")
#print("3. Mostrar el nombre con la primera letra en mayuscula")
#Se solicita que ingrese la opcion
#opcion = int(input("Ingrese la opcion que ddeseas (1 , 2 o 3): "))
#Se pasa el nombre a la opcion elegida por el usuario
#if opcion == 1:
#    print("Tu nombre en mayuscula es: " + nombre.upper())
#elif opcion == 2:
#    print("Tu nombre en minuscula es : " + nombre.lower())
#elif opcion == 3:
#    print("Tu nombtre con la primera letra en mayuscula es: " + nombre.title())
#else:
#    print("opcion invalida. Por favor , elige 1 , 2 o 3.")

#Actividad - 9-
#Maginitud de terroemoto/Clasificacione

#Solicitamos al usuario que ingrese la magnitud del terremoto
#magnitud = float(input("Ingrese la magnitud del terremoto segun la escala de Richter: "))
#Se clasifica la magnitud y se muestra el resultado
#if magnitud < 3:
#    print("Muy leve (imperceptible).")
#elif 3 <= magnitud < 4:
#    print("Leve (ligeramente perceptible).")
#elif 4 <= magnitud < 5:
#    print("Moderado (sentido por personas , pero generalmente no causa daño).")
#elif 5 <= magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras debiles).")
#elif 6 <= magnitud < 7:
#    print("Muy fuerte (puede causar daños significativos).")
#else:
#    print("Extremo (puede causar daños a gran escala).")

#Actividad -10-
# Solicitar al usuario su ubicación y fecha
hemisferio = input("¿En qué hemisferio te encuentras? (N para norte, S para sur): ").upper()
mes = int(input("Ingresa el número del mes actual (1 para enero, 2 para febrero, etc.): "))
dia = int(input("Ingresa el día del mes actual: "))

# Determina la estación según la información proporcionada por el usuario
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio desconocido. Por favor ingresa N o S."

# Mostrar el resultado por pantalla
print(f"La estación en la que te encuentras es: {estacion}")