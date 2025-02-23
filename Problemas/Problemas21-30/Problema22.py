#Problema 22
#Descripción: Este programa simula el lanzamiento de un dado y una moneda.

# Para simular el lanzamiento de una moneda:
import random as rnd
valor = rnd.random()

if valor > 0.50:
    print("Cara de la moneda: águila")
else:
    print("Cara de la moneda: sol")

# Para simular el lanzamiento de un dado:
dado = rnd.randint(1,6)

if dado == 1:
    print("Cara del dado: 1")
if dado == 2:
    print("Cara del dado: 2")
if dado == 3:
    print("Cara del dado: 3")
if dado == 4:
    print("Cara del dado: 4")
if dado == 5:
    print("Cara del dado: 5")
if dado == 6:
    print("Cara del dado: 6")