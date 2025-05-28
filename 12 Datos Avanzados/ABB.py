#Tp integrador Codigo de arbol
# Definición de la clase Nodo para representar cada entrada en el diccionario
class Nodo:
    def __init__(self, palabra, definicion):
        self.palabra = palabra.lower()  # Convertimos a minúsculas para búsquedas sin sensibilidad al caso
        self.definicion = definicion
        self.hijo_izquierdo = None  # Referencia al hijo izquierdo en el árbol binario
        self.hijo_derecho = None  # Referencia al hijo derecho en el árbol binario

    def __str__(self):
        return f"{self.palabra.capitalize()}: {self.definicion}"  # Representación legible del nodo


# Definición de la clase DiccionarioABB, que implementa un diccionario usando un árbol binario de búsqueda
class DiccionarioABB:
    def __init__(self):
        self.raiz = None  # Inicialmente, el árbol está vacío

    # Método para agregar una palabra y su definición al diccionario
    def agregar_palabra(self, palabra, definicion):
        if self.raiz is None:
            self.raiz = Nodo(palabra, definicion)  # Si el árbol está vacío, la palabra se convierte en la raíz
        else:
            self._agregar_recursivo(self.raiz, palabra, definicion)  # Llamada al método recursivo para insertar la palabra

    # Método auxiliar recursivo para insertar una palabra en el árbol binario
    def _agregar_recursivo(self, nodo_actual, palabra, definicion):
        if palabra < nodo_actual.palabra:  # Si la palabra es menor, va a la izquierda
            if nodo_actual.hijo_izquierdo is None:
                nodo_actual.hijo_izquierdo = Nodo(palabra, definicion)
            else:
                self._agregar_recursivo(nodo_actual.hijo_izquierdo, palabra, definicion)
        elif palabra > nodo_actual.palabra:  # Si la palabra es mayor, va a la derecha
            if nodo_actual.hijo_derecho is None:
                nodo_actual.hijo_derecho = Nodo(palabra, definicion)
            else:
                self._agregar_recursivo(nodo_actual.hijo_derecho, palabra, definicion)

    # Método para buscar una palabra en el diccionario
    def buscar_palabra(self, palabra):
        palabra_buscada = palabra.lower()  # Convertimos la palabra a minúsculas para evitar problemas de mayúsculas
        definicion = self._buscar_recursivo(self.raiz, palabra_buscada)
        return definicion if definicion else f"'{palabra}' no se encontró en el diccionario."

    # Método auxiliar recursivo para buscar la palabra en el árbol
    def _buscar_recursivo(self, nodo_actual, palabra_buscada):
        if nodo_actual is None:
            return None  # Si llegamos a un nodo vacío, la palabra no está en el diccionario
        if palabra_buscada == nodo_actual.palabra:
            return nodo_actual.definicion  # Se encontró la palabra, devolvemos la definición
        elif palabra_buscada < nodo_actual.palabra:
            return self._buscar_recursivo(nodo_actual.hijo_izquierdo, palabra_buscada)  # Buscamos en el hijo izquierdo
        else:
            return self._buscar_recursivo(nodo_actual.hijo_derecho, palabra_buscada)  # Buscamos en el hijo derecho

    # Método para listar todas las palabras del diccionario en orden alfabético
    def listar_palabras_inorden(self):
        if self.raiz is None:
            return "El diccionario está vacío."
        lista_palabras = []
        self._inorden_recursivo(self.raiz, lista_palabras)
        return "\n".join(lista_palabras)  # Convertimos la lista en un string con saltos de línea para mejor presentación

    # Método auxiliar recursivo para recorrer el árbol en orden
    def _inorden_recursivo(self, nodo_actual, lista_palabras):
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.hijo_izquierdo, lista_palabras)  # Visitamos el hijo izquierdo
            lista_palabras.append(str(nodo_actual))  # Agregamos el nodo actual a la lista
            self._inorden_recursivo(nodo_actual.hijo_derecho, lista_palabras)  # Visitamos el hijo derecho


# Función para mostrar el menú interactivo
def mostrar_menu():
    print("\n--- Diccionario Interactivo ---")
    print("1. Agregar nueva palabra")
    print("2. Buscar palabra")
    print("3. Mostrar todas las palabras (orden alfabético)")
    print("4. Salir")
    return input("Seleccione una opción: ")


# Función principal que maneja la interacción con el usuario
def main():
    mi_diccionario = DiccionarioABB()  # Se crea una instancia del diccionario
    """"
    # Ejemplo de carga inicial (opcional)
    mi_diccionario.agregar_palabra("Algoritmo", "Secuencia de pasos para resolver un problema.")
    mi_diccionario.agregar_palabra("Python", "Lenguaje de programación interpretado y de alto nivel.")
    mi_diccionario.agregar_palabra("Arbol", "Estructura de datos jerárquica.")
    """
    # Bucle infinito para manejar la interacción con el usuario hasta que se elija salir
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            palabra = input("Ingrese la palabra: ")
            definicion = input("Ingrese la definición: ")
            mi_diccionario.agregar_palabra(palabra, definicion)
            print(f"'{palabra}' agregada al diccionario.")
        elif opcion == '2': 
            palabra = input("Ingrese la palabra a buscar: ")
            nodo_encontrado = mi_diccionario.buscar_palabra(palabra)
            print(f"Definición: {nodo_encontrado}")
        elif opcion == '3':
            print("\n--- Palabras en el Diccionario ---")
            palabras_ordenadas = mi_diccionario.listar_palabras_inorden()
            if palabras_ordenadas:
                print(palabras_ordenadas)  # Imprimimos las palabras ordenadas
            else:
                print("El diccionario está vacío.")
        elif opcion == '4':
            print("Saliendo del diccionario. ¡Hasta luego!")  # Mensaje de despedida
            break
        else:
            print("Opción no válida. Intente de nuevo.")  # Manejo de errores en la entrada del usuario


# Punto de entrada del programa
if __name__ == "__main__":
    main()