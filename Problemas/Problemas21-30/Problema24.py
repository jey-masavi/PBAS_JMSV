#Problema 24
#Descripción: Este programa calcula la suma de una serie numérica.

# Función para calcular la suma de una serie aritmética
def suma_aritmetica(primer_termmino, ultimo_termino, incremento):
    n = (ultimo_termino - primer_termmino) // incremento + 1
    suma = n * (primer_termmino + ultimo_termino) // 2
    return suma

# Función para calcular la suma de una serie geométrica
def suma_geometrica(primer_termino, razon, terminos):
    if razon == 1:
        return primer_termino * terminos
    else:
        return primer_termino * (1 - razon ** terminos) / (1 -razon)

# Función para calcular la suma de una secuencia de número consecutivos
def suma_consecutivos(n):
    return (n * (n + 1)) // 2

# Función principal para interactuar con el usuario
def main():
    print("Opciones de series numéricas:")
    print("1. Suma de números consecutivos (1 + 2 + ... + n)")
    print("2. Suma de una serie aritmética")
    print("3. Suma de una serie geométrica")

    opcion = int(input("Ingrese el tipo de serie que desea sumar (1, 2, 3): "))

    if opcion == 1:
        n = int(input("Ingrese el número hasta el cual desea sumar (n): "))
        print(f"La suma de los números consecutivos de 1 hasta {n} es: {suma_consecutivos(n)}")

    elif opcion == 2:
        primer_termino = int(input("Ingrese el primer término de la serie aritmética: "))
        ultimo_termino = int(input("Ingrese el último término de la serie aritmética: "))
        incremento = int(input("Ingrese el incremento de la serie: "))
        print(f"La suma de la serie arimética es: {suma_aritmetica(primer_termino, ultimo_termino, incremento)}")
    elif opcion == 3:
        primer_termino = int(input("Ingrese el primer término de la serie geométrica: "))
        razon = float(input("Ingrese la razón de la serie geomética: "))
        terminos = int(input("Ingrese el número de términos de la serie: "))
        print(f"La suma de la serie geométrica es: {suma_geometrica(primer_termino, razon, terminos)}")
    else:
        print("Opción no válida. Por favor elija 1, 2 o 3.")

if __name__ == "__main__":
    main()