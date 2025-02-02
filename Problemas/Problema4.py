#Programa 4
#Descripción: Este programa genera la secuencia de Fibonacci hasta un número dada de términos.

n = int(input("Elementos a generar: "))
a, b = 0, 1
if n == 0:
    print(0)
elif n == 0:
    print(b)
else:
    for i in range(0,n):
        print(b)
        c = a + b
        a = b
        b = c