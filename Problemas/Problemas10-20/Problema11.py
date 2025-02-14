#Problema 11
#Descripción: Este programa verifica si una cadena es un palíndromo.

"""Se quitan los espacios (en dado caso si es una frase), las mayúsculas
y las tildes para una mejor maniobrabilidad del programa."""

def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")

    a = 0
    b = len(cadena) - 1

    for i in range(0, len(cadena)):
        if cadena[a] == cadena[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

cadena = input("Ingrese una palabra o frase: ")
if es_palindromo(cadena):
    print("Es un palindromo")
else:
    print("No es un palindromo")