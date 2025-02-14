#Problema 17
#Descripción: Este programa implementa estructuras de datos básicas: pila, cola y lista enlazada.

"""Funciones para Pila"""
def pila_apilar(pila, item):
    # Agrega un elemento a la pila
    pila.append(item)

def pila_desapilar(pila):
    # Elimina y retorna el último elemento agregado a la pila
    if pila:
        return pila.pop()
    else:
        print("La pila está vacía, no se puede desapilar")
        return None
    
def pila_cima(pila):
    # Retorna el último elemento de la pila sin eliminarlo
    if pila:
        return pila[-1]
    else:
        print("La pila está vacía")
        return None
    
def pila_tamannio(pila):
    # Retorna el número de elementos en la pila
    return len(pila)

def pila_mostrar(pila):
    # Muestra todos los elementos de la pila
    if pila:
        print("Contenido de la pila:", pila)
    else:
        print("La pila está vacía")

"""Funciones para Cola"""
def cola_encolar(cola, elemento):
    # Añade un elemento al final de la cola
    cola.append(elemento)

def cola_desencolar(cola):
    # Quita el primer elemento de la cola
    if cola:
        return cola.pop(0)
    else:
        print("La cola está vacía")
        return None
    
def cola_mostrar(cola):
    # Muestra todos los elementos de la cola
    print("Cola:", cola)

"""Funciones para Lista Enlazada"""
def lista_enlazada_insertar_inicio(lista, valor):
    # Inserta un valor al inicio de la lista
    lista.insert(0, valor)

def lista_enlazada_insertar_final(lista, valor):
    # Inserta un valor al final de la lista
    lista.append(valor)

def lista_enlazada_eliminar(lista, valor):
    # Elimina el primer elemento que tenga el valor dado
    if valor in lista:
        lista.remove(valor)
    else:
        print("Elemento no encontrado")

def lista_enlazada_mostrar(lista):
    # Muestra todos los elementos de la lista
    if lista:
        print("Lista:", " -> ".join(map(str, lista)))
    else:
        print("La lista está vacía")

"""Ejemplo de uso de las tres estructuras"""

# Uso de Pila
print("Ejemplo de uso de Pila")
pila = []
pila_apilar(pila, 10)
pila_apilar(pila, 20)
pila_apilar(pila, 30)
pila_mostrar(pila)
print("Elemento desapilado:", pila_desapilar(pila))
pila_mostrar(pila)
print("Tamaño de la pila:", pila_tamannio(pila))
print("Elemento de la cima:", pila_cima(pila))

# Uso de Cola
print("\nEjemplo de uso de Cola")
cola = []
cola_encolar(cola, 10)
cola_encolar(cola, 20)
cola_encolar(cola, 30)
cola_mostrar(cola)
print("ELemento desencolado:", cola_desencolar(cola))
cola_mostrar(cola)

# Uso de Lista Enlazada
print("\nEjemplo de uso de Lista Enlazada")
lista = []
lista_enlazada_insertar_inicio(lista, 10)
lista_enlazada_insertar_inicio(lista, 20)
lista_enlazada_insertar_inicio(lista, 30)
lista_enlazada_mostrar(lista)
lista_enlazada_insertar_final(lista, 40)
lista_enlazada_insertar_final(lista, 50)
lista_enlazada_mostrar(lista)
lista_enlazada_eliminar(lista, 20)
lista_enlazada_mostrar(lista)
lista_enlazada_eliminar(lista, 100)
lista_enlazada_mostrar(lista)