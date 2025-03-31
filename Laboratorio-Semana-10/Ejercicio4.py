# Ejercicio 4: Calculadora de Estadísticas
"""Descripción: Este programa solicita al usuario una lista de números y muestra lo siguiente:
 * Promedio, mediana y desviación estándar.
 * Permite un número arbitrario de argumentos.
 * Realiza cálculos simples como la media."""

import statistics

def calcular_estadisticas(*args):
    # Promedio utilizando lambda
    promedio = lambda nums: sum(nums) / len(nums) if len(nums) > 0 else 0
    
    # Mediana utilizando la librería statistics
    mediana = statistics.median(args)
    
    # Desviación estándar utilizando la librería statistics
    desviacion_estandar = statistics.stdev(args) if len(args) > 1 else 0
    
    return promedio(args), mediana, desviacion_estandar

# Solicitar al usuario ingresar los números
entrada = input("Introduce una lista de números separados por comas: ")
numeros = list(map(float, entrada.split(',')))

# Llamar a la función con los números proporcionados
promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)

# Mostrar los resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion_estandar}")