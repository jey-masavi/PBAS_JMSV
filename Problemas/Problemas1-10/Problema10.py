#Problema 10
#Descripción: Aquí se leerá, escribirá y modificará un archivo de texto.

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)