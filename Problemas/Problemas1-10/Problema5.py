#Problema 5
#Descripción: Este programa verifica si un número es primo.

num = int(input("Ingrese un número: "))
x = 1
c = 0
while x<= num:
    if num % x == 0:
        c = c + 1
    x = x + 1
if c == 2:
    print("El número ", num, " es primo")
else:
    print("El número ", num, " no es primo")