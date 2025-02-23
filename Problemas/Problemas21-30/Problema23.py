#Problema 23
#Descripción: Este programa implementa y opera con matrices.

# Función para imprimir una matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para ingresar una matriz
def ingresar_matriz(filas, columnas):
    matriz = []
    print(f"Ingrese los elementos de la matriz de {filas}x{columnas}:")
    for i in range(filas):
        while True:
            fila = list(map(int, input(f"Ingrese la fila {i+1} (separada por espacios): ").split()))
            if len(fila) == columnas:
                matriz.append(fila)
                break
            print(f"La fila debe tener exactamente {columnas} elementos. Inténtelo de nuevo.")
    return matriz

# Función genérica para sumar o restar matrices
def operar_matrices(matriz1, matriz2, operacion):
    return [[operacion(m1, m2) for m1, m2 in zip(f1, f2)] for f1, f2 in zip(matriz1, matriz2)]

# Funciones para operacines específicas
def suma(m1,m2):
    return m1 + m2

def resta(m1,m2):
    return m1 - m2

# Función para multiplicar matrices
def multiplicacion_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("No se puede multiplicar las matrices: las dimensiones no son compatibles.")
    return [[sum(a * b for a, b in zip(fila_matriz1, columna_matriz2)) for columna_matriz2 in zip(*matriz2)] for fila_matriz1 in matriz1]

# Función para transponer una matriz
def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]

# Función principal para interactuar con el usuario
def main():
    print("Operaciones con matrices")

    filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
    columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))
    matriz1 = ingresar_matriz(filas1, columnas1)

    filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
    columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
    matriz2 = ingresar_matriz(filas2, columnas2)

    print("\nMatriz 1:")
    imprimir_matriz(matriz1)
    print("\nMatriz 2:")
    imprimir_matriz(matriz2)

    if filas1 == filas2 and columnas1 == columnas2:
        print("\nSuma de matrices:")
        imprimir_matriz(operar_matrices(matriz1, matriz2, suma))

        print("\nResta de matrices:")
        imprimir_matriz(operar_matrices(matriz1, matriz2, resta))
    else:
        print("\nNo se pueden realizar la suma ni la resta de las matrices, ya que tienen dimensiones diferentes.")
    if columnas1 == filas2:
        print("\nMultiplicación de matrices:")
        imprimir_matriz(multiplicacion_matrices(matriz1, matriz2))
    else:
        print("\nNo se pueden multiplicar las matrices, ya que el número de columnas de la primera matriz no es igual al número de filas de la segunda.")
    
    print("\nTransposición de la matriz 1:")
    imprimir_matriz(transponer_matriz(matriz1))

    print("\nTransposición de la matriz 2:")
    imprimir_matriz(transponer_matriz(matriz2))


if __name__ == "__main__":
    main()