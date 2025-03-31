# Ejercicio 8: Implementación de Mergesort.
"""Descripción: Este programa implementa el algoritmo de Mergesort para ordenar una lista de números 
ingresada por el usuario, además, muestra la lista antes y después del ordenamiento."""

# Función de Mergesort
def mergesort(lista):
    if len(lista) > 1:
        # Dividir la lista en dos mitades
        medio = len(lista) // 2
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]

        # Ordenar recursivamente las dos mitades
        mergesort(mitad_izquierda)
        mergesort(mitad_derecha)

        # Mezclar las dos mitades ordenadas
        i = j = k = 0

        # Combinar las dos mitades ordenadas
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Si quedan elementos en la mitad izquierda
        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # Si quedan elementos en la mitad derecha
        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

# Programa principal
def main():
    # Ingresar la lista de números
    lista = input("Ingrese una lista de números separados por espacios: ").split()
    
    # Convertir los números ingresados en enteros
    lista = [int(x) for x in lista]
    
    # Mostrar la lista antes del ordenamiento
    print(f"Lista antes de ordenar: {lista}")
    
    # Ordenar la lista con Mergesort
    mergesort(lista)
    
    # Mostrar la lista después del ordenamiento
    print(f"Lista después de ordenar: {lista}")

# Ejecutar el programa
if __name__ == "__main__":
    main()