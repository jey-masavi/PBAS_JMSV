#Problema 19
#Descripción: Este programa genera números aleatorios con distintas distribuciones.

import random
import math

"""Función para generar una distribución uniforme"""
#  Se generan números aleatorios dentro de un intervalo, todos con la misma probabilidad de ocurrir.
def distribucion_uniforme(low, high, size):
    return [random.uniform(low, high) for _ in range(size)]

"""Función para generar una distribución normal usando Box-Muller"""
#  Usando el método de Box-Muller a partir de dos números aleatorios uniformes, se generan números
#  con una distribución en forma de campana (media y desviación estándar).
def distribucion_normal(mu, sigma, size):
    random_numbers = []
    for _ in range(size // 2):
        u1 = random.random()
        u2 = random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
        random_numbers.append(mu + z0 * sigma)
        random_numbers.append(mu + z1 * sigma)
    return random_numbers[:size]

"""Función para generar una distribución exponencial"""
#  Se genera números que siguen una tasa constante de ocurrencia de eventos (basado en un parámetro lambda).
def distribucion_exponencial(lam, size):
    return[random.expovariate(lam) for _ in range(size)]

"""Función para generar una distribución binomial"""
#  Simula n ensayos independientes (con solo dos resultados posibles) y cuenta cuántos son exitosos, con
#  probabilidad p de éxito.
def distribucion_binomial(n, p, size):
    return[random.binomialvariate(n, p) for _ in range(size)]

"""Función para generar uns distribución de Poisson"""
#  Se genera la cantidad de eventos que ocurren en un intervalo de tiempo o espacio, con una tasa promedio
#  constante.
def distribucion_poisson(lam, size):
    random_numbers = []
    for _ in range(size):
        L = math.exp(-lam)
        p = 1.0
        k = 0
        while p > L:
            k += 1
            p *= random.random()
        random_numbers.append(k - 1)
    return random_numbers

# Generar distribuciones
size = 100
uniform = distribucion_uniforme(0, 10, size)
normal = distribucion_normal(0, 1, size)
exponential = distribucion_exponencial(1, size)
binomial = distribucion_binomial(10, 0.5, size)
poisson = distribucion_poisson(5, size)

# Mostrar algunos de los resultados
print("Distribución Uniforme:", uniform[:10])
print("Distribución Normal:", normal[:10])
print("Distribución Exponencial:", exponential[:10])
print("Distribución Binomial:", binomial[:10])
print("Distribución de Poisson:", poisson[:10])