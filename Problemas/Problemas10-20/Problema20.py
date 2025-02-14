#Problema 20
#Descripción: Este programa implementa búsqueda binaria y lineal.

from random import randint

listaP = list()
listaN = list()
elementos = int(input("Introduzca la cantidad de elementos: "))

for count in range(-elementos, elementos):
    if count < 0:
        listaN.append(randint(-100, 0))
    elif count > 0:
        listaP.append(randint(1, 100))
    else:
        listaP.append(randint(0, 1))

# Sumar las listas para obtener la lista completa
listaCompleta = listaN + listaP
# Ordenar la lista para la búsqueda binaria
listaOrdenada = sorted(listaCompleta)

print("Lista completa sin ordenar:", listaCompleta)
print("Lista ordena:", listaOrdenada)

"""Función de búsqueda binaria"""
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1 # Si no se encuentra el número

"""Función de búsqueda lineal"""
def busqueda_lineal(lista, objetivo):
    for index, itm in enumerate(lista):
        if itm == objetivo:
            return index
    return -1 # Si no se encuentra ek número

# Elegir el tipo de búsqueda
opcion = input("Elija el tipo de búsqueda (binaria/lineal): ").lower()

num = int(input("Introduzca un número a buscar: "))

if opcion == "binaria":
    resultado = busqueda_binaria(listaOrdenada, num)
    if resultado != -1:
        print(f"El número {num} se encuentra en la posición {resultado} (búsqueda binaria).")
    else:
        print(f"El número {num} no se encuentra en la lista (búsqueda binaria).")

elif opcion == "lineal":
    resultado = busqueda_lineal(listaCompleta, num)
    if resultado != -1:
        print(f"El número {num} se encuentra en la posición {resultado} (búsqueda lineal).")
    else:
        print(f"El número {num} no se encuentra en la lista (búsqueda lineal).")

else:
    print("Opción no válida, Por favor, elija 'binaria' o 'lineal'.")