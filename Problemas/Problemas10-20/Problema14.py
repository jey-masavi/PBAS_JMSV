#Problema 14
#Descripción: Este programa implementa distintos métodos de ordenamiento.

"""Función de ordenamiento por burbuja (Bubble Sort), que consiste en comparar
elementos adyacentes y los intercambia si están en el orden incorrecto."""
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


"""Función de ordenamiento por inserción (Insertion Sort), toma un elemento y lo
inserta en la posición correcta respecto a los elementos anteriores."""
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista


"""Función de ordenamiento rápido (Quick Sort), utiliza un pivote para dividir el
arreglo en dos subarreglos y luego los ordena de manera recursiva."""
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    left = [x for x in lista if x < pivot]
    middle = [x for x in lista if x == pivot]
    rigth = [x for x in lista if x > pivot]
    return quick_sort(left) + middle +quick_sort(rigth)


"""Función de ordenamiento por selección (Selection Sort), encuentra el elemento
mínimo en el arreglo y lo coloca en la posición correcta."""
def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = 1
        for j in range (i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


"""Función de ordenamiento por mezcla (Merge Sort), divide el arreglo en mitades,
ordena cada mitad y luego las combina."""
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1
    return lista


# Función principal para probar los métodos.
def main():
    lista = [17, 25, 197, 8, 50, 88, 99, 13, 7, 222]
    print("Arreglo original:", lista)

    print("\nOrdenamiento por Burbuja:")
    print(bubble_sort(lista.copy()))

    print("\nOrdenamiento por Inserción:")
    print(insertion_sort(lista.copy()))

    print("\nOrdenamiento Rápido:")
    print(quick_sort(lista.copy()))

    print("\nOrdenamiento por Selección:")
    print(selection_sort(lista.copy()))

    print("\nOrdenamiento por Mezcla:")
    print(merge_sort(lista.copy()))

if __name__ == "__main__":
    main()