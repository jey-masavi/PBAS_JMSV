#Problema 7
#Descripión: Este programa determina si un número es par, impar o múltiplo de otro.

num1 = int(input("Ingrese un número: "))
if num1 % 2 == 0:
    print("El número ", num1, " es par")
else:
    print("El número ", num1, " es impar")

def calcular(x,y):
    if x % y == 0:
        print(f"{x} es múltiplo de {y}")
    elif y % x == 0:
        print(f"{y} es múltiplo de {x}")
    else:
        print("Los números no son múltiplos")

num2 = int(input("Ingrese otro número: "))
calcular(num1, num2)