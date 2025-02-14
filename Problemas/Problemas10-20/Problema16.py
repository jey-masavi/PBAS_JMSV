#Problema 16
#Descripción: Este programa cuenta el número de vocales y consonantes en una cadena.

cadena = input("Ingrese una palabra o frase: ")
vocales = "aeiouAEIOU"
a = 0
b = 0
for i in cadena:
    if ord(i) >= 65 and ord(i) <= 122:
        if i in vocales:
            a += 1
        else:
            b += 1
print(f"Vocales: {a}")
print(f"Consonantes: {b}")