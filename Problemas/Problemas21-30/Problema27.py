#Problema 27
#Descripción: Este programa es un conversor de unidades.

def convertir_longitud():
    print("\nConversor de Longitud:")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    opcion = int(input("Seleccione la opcion (1 o 2): "))

    if opcion == 1:
        metros = float(input("Introduzca la cantidad en metros: "))
        print(f"{metros} metros es igual a {metros/1000} kilómetros.")
    elif opcion == 2:
        kilometros = float(input("Introduzca la cantidad en kilómetros: "))
        print(f"{kilometros} kilométros es igual a {kilometros * 1000} metros.")
    else:
        print("Opción no válida.")

def convertir_peso():
    print("\nConversor de Peso:")
    print("1. Gramos a Kilogramos")
    print("2. Kilogramos a Gramos")
    opcion = int(input("Seleccione la opción (1 o 2): "))

    if opcion == 1:
        gramos = float(input("Introduzca la cantidad en gramos: "))
        print(f"{gramos} gramos es igual a {gramos / 1000} kilogramos.")
    elif opcion == 2:
        kilogramos = float(input("Introduzca la cantidad en kilogramos: "))
        print(f"{kilogramos} kilogramos es igual a {kilogramos * 1000} gramos.")
    else:
        print("Opción no válida.")

def convertir_temperatura():
    print("\nConversor de Temperatura:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = int(input("Seleccione la opción (1 o 2): "))

    if opcion == 1:
        celsius = float(input("Introduzca la temperatura en Celsius: "))
        print(f"{celsius}° Celsius es igual a {(celsius * 9/5) + 32}° Fahrenheit.")
    elif opcion == 2:
        fahrenheit = float(input("Introduzca la temperatura en Fahrenheit: "))
        print(f"{fahrenheit}° Fahrenheit es igual a {(fahrenheit - 32) * 5/9}° Celsius.")
    else:
        print("Opción no válida.")

def main():
    while True:
        print("\nCONVERSOR DE UNIDADES")
        print("1. Convertir Longitud")
        print("2. Convertir Peso")
        print("3. Convertir Temperatura")
        print("4. Salir")

        opcion = int(input("Seleccione la opción (1-4): "))

        if opcion == 1:
            convertir_longitud()
        elif opcion == 2:
            convertir_peso()
        elif opcion == 3:
            convertir_temperatura()
        elif opcion == 4:
            print("Saliendo del conversor de unidades...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()