#Problema 18
#Descripción: Este programa resuelve ecuaciones cuadráticas.

import math

print("Calculadora para ecuaciones de segundo grado")
print("________________________________________________________")
print("Teniendo en cuenta la forma de la ecuación ax^2 + bx + c")
print("________________________________________________________")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

"""Calcular el discriminante"""
d = (b**2) - 4 * a * c

"""Comprobar y calcular"""
if d < 0:
    print("No existen soluciones reales.")
else:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)

    print("---- Soluciones ----")
    print("Solucion x1: ", x1)
    print("Solución x2: ", x2)