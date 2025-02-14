#Problema 3
#Descripción: Este programa calcula el factorial de un número dado.

num = int(input("Ingrese un número: "))
fact = 1
if num!=0:
    for i in range(1,num+1):
        fact = fact * i
print("Factorial: ", fact)