#Problema 29
#Descripción: Este programa genera y analiza datos estadísticos.

import random
import statistics

# Función para generar datos aleatorios
def generar_datos(cantidad, min_valor, max_valor):
    return [random.randint(min_valor, max_valor) for _ in range(cantidad)]

# Función para mostrar los análisis estadísticos
def analizar_datos(datos):
    print("\nAnálisis estadísticos de los datos:")

    # Media
    media = statistics.mean(datos)
    print(f"Media: {media:.2f}")

    # Mediana
    mediana = statistics.median(datos)
    print(f"Mediana: {mediana}")

    # Moda
    try:
        moda = statistics.mode(datos)
        print(f"Moda: {moda}")
    except statistics.StatisticsError:
        print("Moda: No hay moda (valores múltiples)")

    # Desviación estándar
    desviacion_estandar = statistics.stdev(datos)
    print(f"Desviación estándar: {desviacion_estandar:.2f}")

    # Rango
    rango = max(datos) - min(datos)
    print(f"Rango: {rango}")

    # Cuartiles
    cuartil_1 = statistics.quantiles(datos, n = 4)[0]
    cuartil_2 = statistics.median(datos)
    cuartil_3 = statistics.quantiles(datos, n = 4)[2]
    print(f"Cuartil 1: {cuartil_1}")
    print(f"Cuartil 2 (Mediana): {cuartil_2}")
    print(f"Cuartil 3: {cuartil_3}")

# Función principal para ejecutar el programa
def main():
    cantidad = int(input("¿Cuántos datos quiere generar?: "))
    min_valor = int(input("Valor mínimo: "))
    max_valor = int(input("Valor máximo: "))

    # Se genera los datos aleatorios
    datos = generar_datos(cantidad, min_valor, max_valor)
    print(f"\nDatos generados: {datos}")

    # Se realiza el análisis estadístico
    analizar_datos(datos)

if __name__ == "__main__":
    main()