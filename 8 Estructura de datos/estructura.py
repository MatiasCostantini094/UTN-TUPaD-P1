#Trabajo Practico N6 Estructura de datos Complejas
"""
#Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas con sus respectivos precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
# print(precios_frutas) Se comenta para ej 2

#Actividad 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Mostrar el diccionario actualizado
# print("Precios actualizados:", precios_frutas) Se comenta para ej 3

#Activdad 3
# Crear la lista de frutas sin precios
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print("Lista de frutas:", lista_frutas)
"""
#Actividad 4
"""
# Crear el diccionario para almacenar contactos
contactos = {}

# Cargar 5 contactos

for _ in range(5):
    nombre = input("Introduce el nombre del contacto: ")
    numero = input("Introduce el número telefónico: ")
    contactos[nombre] = numero

# Consultar un número telefónico
nombre_consulta = input("Introduce el nombre a buscar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es {contactos[nombre_consulta]}")
else:
    print("El contacto no está registrado.")
"""
# Actividad 5
"""
def procesar_frase(frase):
    palabras = frase.lower().split()  # Convertir a minúsculas y dividir en palabras
    palabras_unicas = set(palabras)  # Obtener palabras únicas
    recuento = {}  # Diccionario para contar ocurrencias

    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1

    return palabras_unicas, recuento

# Solicitar entrada al usuario
frase = input("Introduce una frase: ")

# Procesar la frase y mostrar resultados
unicas, conteo = procesar_frase(frase)
print("Palabras únicas:", unicas)
print("Recuento de palabras:", conteo)
"""
# Actividad 6
"""
# Crear el diccionario para almacenar alumnos y sus notas
alumnos = {}

# Cargar 3 alumnos y sus 3 notas
for _ in range(3):
    nombre = input("Introduce el nombre del alumno: ").strip()
    notas = tuple(map(int, input(f"Introduce las 3 notas de {nombre}, separadas por espacios: ").split()))
    alumnos[nombre] = notas

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
"""
#Actividad 7
"""
# Listas de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {101, 102, 103, 104, 105}
aprobados_parcial2 = {103, 104, 106, 107, 105}

# 1. Estudiantes que aprobaron ambos parciales (intersección)
aprobados_ambos = aprobados_parcial1 & aprobados_parcial2

# 2. Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
aprobados_solo_uno = aprobados_parcial1 ^ aprobados_parcial2

# 3. Estudiantes que aprobaron al menos un parcial (unión)
aprobados_al_menos_uno = aprobados_parcial1 | aprobados_parcial2

# Mostrar resultados
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
print("Estudiantes que aprobaron solo uno de los dos:", aprobados_solo_uno)
print("Total de estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)
"""
#Actividad 8
# Crear diccionario de productos y su stock
"""
stock_productos = {}

while True:
    print("\nOpciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        producto = input("Introduce el nombre del producto: ").strip()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no está registrado.")

    elif opcion == "2":
        producto = input("Introduce el nombre del producto a modificar: ").strip()
        if producto in stock_productos:
            cantidad = int(input("Introduce la cantidad a agregar: "))
            stock_productos[producto] += cantidad
            print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no está registrado.")

    elif opcion == "3":
        producto = input("Introduce el nombre del nuevo producto: ").strip()
        if producto in stock_productos:
            print("El producto ya existe en el stock.")
        else:
            cantidad = int(input("Introduce la cantidad inicial: "))
            stock_productos[producto] = cantidad
            print(f"{producto} agregado con {cantidad} unidades.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")
"""
#Actividad 9
"""
# Crear diccionario para la agenda
agenda = {}

# Función para agregar un evento
def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento

# Función para consultar un evento
def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay eventos programados.")

# Cargar algunos eventos
agregar_evento("Lunes", "10:00", "Reunión de equipo")
agregar_evento("Martes", "14:30", "Clase de Python")
agregar_evento("Viernes", "18:00", "Cena con amigos")

# Consulta de eventos
dia_consulta = input("Introduce el día: ").strip()
hora_consulta = input("Introduce la hora: ").strip()

print(f"Evento en {dia_consulta} a las {hora_consulta}: {consultar_evento(dia_consulta, hora_consulta)}")
"""
# Actividad 10
"""
paises_capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)
"""