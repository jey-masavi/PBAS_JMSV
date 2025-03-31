# Ejercicio 5: Módulo para Conversión de Unidades
"""Descripción: Este programa importa un módulo llamado 'conversor.py' y permite al usuario 
realizar las siguientes conversiones:
 * Kilómetros a millas
 * Celsius a Fahrenheit
 * Litros a galones"""

# Programa prinicipal
import conversor

def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("Selecciona una opción para realizar la conversión:")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            km = float(input("Ingresa la distancia en kilómetros: "))
            print(f"{km} kilómetros son {conversor.km_a_millas(km)} millas.\n")
        elif opcion == "2":
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            print(f"{celsius} grados Celsius son {conversor.celsius_a_fahrenheit(celsius)} grados Fahrenheit.\n")
        elif opcion == "3":
            litros = float(input("Ingresa la cantidad de litros: "))
            print(f"{litros} litros son {conversor.litros_a_galones(litros)} galones.\n")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.\n")

if __name__ == "__main__":
    main()