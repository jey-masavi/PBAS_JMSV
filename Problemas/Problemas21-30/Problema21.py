#Problema 21
#Descripción: Este programa calcula el área y volumen de distintas figuras geométricas.

import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_cuadrado(lado):
    return lado** 2

def area_triangulo(base,altura):
    return(base * altura) / 2

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio ** 2 * altura

def volumen_esfera(radio):
    return (3/4) * math.pi * radio ** 3

def main():
    print("Seleccione una figura geométrica:")
    print("1. Círculo ")
    print("2. Cuadrado")
    print("3. Triángulo")
    print("4. Cilindro")
    print("5. Cono")
    print("6. Esfera")

    opcion = int(input("Ingrese el número de la figura: "))

    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        print(f"El área del cuadrado es: {area_cuadrado(lado)}")
    elif opcion == 3:
        base = float(input("Ingrese la base del trángulo: "))
        altura = float(input("Ingrese la altura del trángulo: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura)}")
    elif opcion == 4:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura)}")
    elif opcion == 5:
        radio = float(input("Ingrese el radio del cono: "))
        altura = float(input("Ingrese la altura del cono: "))
        print(f"El volumen del cono es: {volumen_cono(radio, altura)}")
    elif opcion == 6:
        radio = float(input("Ingrese el radio de la esfera: "))
        print(f"El volumen de la esfera es: {volumen_esfera(radio)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()