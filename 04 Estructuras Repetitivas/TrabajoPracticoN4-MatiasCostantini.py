# Trabajo Practico N4  Estructuras repetitivas
#Matias Costantini 
"""
# Actividad 1
print("Este programa imprime los valores de 0 a 100 , en orden creciente")          # Mensaje en pantalla
cont = 0                 #contador iniciado en 0
while cont <= 100:      #Condicion de bucle , indica que el contador debe ser menor o igual a 100
    print(cont)         #Se imprime el contador
    cont += 1           #Acumulador de contador
"""

#Actividad 2
""""
#Se pide al usuario que ingrese un numero entero
numero = input("Ingrese un numero entero: ") 
contador = 0                                             # se indica el contador en 0

for caracter in numero:
    if caracter.isdigit():                              # Se asegura que cuente solo los digitos
        contador += 1                                   #es el acumulador del contador

print(f"EL numero tiene {contador} digitos. ")          # se llama a la funcion

"""
#Actividad 3
"""
#Se pide al usuario que ingrese 2 numeros
numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el segundo numero"))
# se establece el orden correcto de los valores para realizar la suma 
if numero1 > numero2:
    numero1, numero2 =numero2 , numero1
suma = 0
for i in range(numero1 + 1, numero2):                                        # se suma los numeros dados entre los indicados , sin contar los extremos
    suma += i

print(f"La suma de los numeros entre {numero1} y {numero2} , sin contar los extremos , es: {suma}")         # se llama a la funcion
"""
#Actividad 4
"""
print("Ingrese el numero que desea para acumular y 0 para salir \n")      #Mensaje de salida 
suma = 0                                                                  #Se establece el acumulador en 0 
while True:                                                               #Se crea un bucle infinito , hasta que se encuentre con la condicion de 0 
    numero = int(input("Ingrese un numero "))                             #Se le pide al usuario que ingrese el numero
    if numero == 0:                                                       #Condicion para que el numero no sea 0
        print("La suma acumulada total fue \n ", suma)                    #Mensaje para cuando se cumpla la condicion de numero 0 , da la suma total acumulada
        break                                                             #Despues del Mensaje , corta el bucle infinito 
    suma += numero                                                        #Actualiza el acumulador 
        
    print("Suma acumulada \n",suma)                                       # Se imprime la suma parcial acumulada 
"""
#Actividad 5
""""
import random

print("Juguemos a adivinar el numero \n")                               #Mensaje para el usuario
numero = int(input("Elige un numero entre 0 y 9 \n"))
intento = 0                                                          #Se establece el intento en 0 / acumulador
while numero >= 0 and numero <= 9:                                   #Condicion para que el numero este entre 0 y 9
    numero_aleatorio = random.randint(0, 9)                          #Se genera un numero aleatorio entre 0 y 9
    intento += 1                             
    if numero == numero_aleatorio:                                      #Condicion para que el numero ingresado por el usuario sea igual al numero aleatorio
        print(f"Felicidades, adivinaste el numero era el {numero_aleatorio} y nada mas te llevo {intento}")  #Mensaje de felicitacion
        break
    else:
       numero = int(input("No acertaste. Elige otro numero entre 0 y 9 \n"))  #Si no acierta, se le pide que ingrese otro numero
"""

#Actividad 6
"""
print("Este programa imprime los valores pares de 0 a 100 , en orden decreciente")          # Mensaje en pantalla
cont = 100                 #contador iniciado en 100
while cont >= 0:      #Condicion de bucle , indica que el contador debe ser mayor o igual a 0
    print(cont)         #Se imprime el contador
    cont -= 2           #Acumulador de contador de manera decreciente
"""
#Actividad 7
"""
print("Sumemos unos numeros \n")                              #Mensaje para el usuario

suma = 0                                                      # Suma/ contador establecido en 0
numero = int(input("Ingrese un numero Mayor que 0 \n"))       # Se le solicita que ingrese un numero mayor que 0                                                    
for i in range(0,numero):                                     #Se establece el rango de 0 al numero que indique el usuario
        suma += i                                             #El acumulador 
print(f"La suma de los numeros comprendidos entre el 0 y {numero} es : \n {suma}") #Mensajeecon el resultado final
"""
#Actividad 8 

#Actividad 9

#Actividad 10
"""
print("Juguemos a dar vuelta los numeros \n")               #Mensaje para el usuario
numero = (input("Ingrese el numero positivo que guste \n")) # Se pide que ingrese un numero 
if numero.isdigit():                                        #Se verifica que el contenido de la variable sean numeros
    numero_intertido = numero[::-1]                         #Utilizamos el slicig de cadenas para invertir el orden
    print(f"El numero invertido es : {numero_intertido}")   #   se imprime el resultado con un mensaje
else:
    print("No ingreso numeros enteros")                     #Se avisa que lo que ingreso no es correcto
"""