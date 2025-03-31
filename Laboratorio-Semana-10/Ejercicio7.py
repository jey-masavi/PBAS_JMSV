#  Ejercicio 7: Ordenamiento y Búsqueda.
"""Descripción: Este programa implementa lo siguiente:
 * Genera una lista de números aleatorios.
 * Ordena la lista usando el algoritmo de Quicksort.
 * Permite al usuario buscar un número en la lista usando búsqueda binaria.
El programa muestra la lista antes y después del ordenamiento y los resultados de la búsqueda."""

import random

# Función para generar una lista de números aleatorios
def generar_lista(tamaño, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

# Algoritmo de Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivot]
    iguales = [x for x in lista if x == pivot]
    mayores = [x for x in lista if x > pivot]
    return quicksort(menores) + iguales + quicksort(mayores)

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio + 1 # Ajustar para contar desde 1
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1  # Si no se encuentra el número

# Programa principal
def main():
    tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
    rango_min = int(input("Ingrese el valor mínimo para los números: "))
    rango_max = int(input("Ingrese el valor máximo para los números: "))

    # Generar la lista aleatoria
    lista = generar_lista(tamaño_lista, rango_min, rango_max)
    print(f"Lista generada: {lista}")
    
    # Ordenar la lista con Quicksort
    lista_ordenada = quicksort(lista)
    print(f"Lista ordenada: {lista_ordenada}")
    
    # Buscar un número en la lista
    numero_buscado = int(input("Ingrese el número a buscar: "))
    
    # Realizar búsqueda binaria en la lista ordenada
    resultado = busqueda_binaria(lista_ordenada, numero_buscado)
    
    if resultado != -1:
        print(f"El número {numero_buscado} se encuentra en la posición {resultado} de la lista ordenada.")
    else:
        print(f"El número {numero_buscado} no se encuentra en la lista.")
    
# Ejecutar el programa
if __name__ == "__main__":
    main()