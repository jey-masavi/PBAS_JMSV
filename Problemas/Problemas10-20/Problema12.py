#Problema 12
#Descripción: Este programa encuentra el mayor entre tres números dados.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a != b and a!= c and b != c:
    if a > b:
        if a > c:
            print("El numero mayor es:", a)
        else:
            print("El numero mayor es:", c)
    else:
        if b > c:
            print("El numero mayor es:", b)
        else:
            print("El numero mayor es:", c)
else:
    print("Ingrese tres números diferentes.")