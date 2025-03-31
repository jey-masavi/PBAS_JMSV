# Ejercicio 1: Análisis de texto con diccionarios y conjuntos.
""" Descripción: Este programa analiza un texto ingresado por el usuario y determina:
 * El número total de palabras en el texto
 * La cantidad de palabras únicas, utilizando un conjunto para evitar repeticiones.
 * La frecuencia de cada palabra usando un diccionario donde la clave sea la palabra
   y el valor la cantidad de veces que aparece.
 * La palabra más frecuente y cuántas veces aparece.
El programa muestra un resumen con los datos anteriores."""

def analizar_texto(texto):
    # Convertir todo el texto a minísculas y se divide en palabras
    palabras = texto.lower().split()
    
    # Número total de palabras
    total_palabras = len(palabras)

    # Conjunto de palabras únicas
    palabras_unicas = set(palabras)

    # Frecuencia de cada palabra en un diccionario
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    # Encontrar la palabra más frecuente
    palabra_mas_frecuente = max(frecuencia, key = frecuencia.get)
    frecuencia_max = frecuencia[palabra_mas_frecuente]

    # Mostrar los resultados
    print("Resumen del ánalisis:")
    print(f"1. Número total de palabras: {total_palabras}")
    print(f"2. Número de palabras únicas: {len(palabras_unicas)}")
    print(f"3. Frecuencia de cada palabra:")
    for palabra, count in frecuencia.items():
        print(f"    - {palabra}: {count}")
    print(f"4. La palabra más frecuente es '{palabra_mas_frecuente}' que aparece {frecuencia_max} veces.")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingrese un texto para analizar: ")
analizar_texto(texto_usuario)