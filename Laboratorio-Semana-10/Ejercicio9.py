#  Ejercicio 9: Implementación de Múltiples Paradigmas.
"""Descripción: Este programa implementa y demuestra diferentes paradigmas de programación:
 * Imperativa: Uso de estructuras de control como condicionales y bucles.
 * Estructurada: Separa el código en funciones bien definidas.
 * Modular: Crear diferentes módulos para funcionalidades específicas.
 * Orientada a Objetos: Definir clases y objetos."""

# Programa principal
import tareas  # Importar el módulo de tareas

# Función para mostrar el menú (paradigma estructurado)
def mostrar_menu():
    print("\nGestor de Tareas:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

# Función principal del programa (paradigma estructurado)
def ejecutar_programa():
    tareas_lista = []  # Lista de tareas (paradigma imperativo)
    
    while True:  # Bucle de ejecución continua (paradigma imperativo)
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tareas.mostrar_tareas(tareas_lista)  # Llamada a la función modularizada
        elif opcion == "2":
            descripcion = input("Ingresa la descripción de la tarea: ")
            tareas.agregar_tarea(tareas_lista, descripcion)  # Llamada a la función modularizada
        elif opcion == "3":
            descripcion = input("Ingresa la descripción de la tarea a eliminar: ")
            tareas.eliminar_tarea(tareas_lista, descripcion)  # Llamada a la función modularizada
        elif opcion == "4":
            descripcion = input("Ingresa la descripción de la tarea a marcar como completada: ")
            tarea = next((tarea for tarea in tareas_lista if tarea.descripcion == descripcion), None)
            if tarea:
                tarea.marcar_completada()  # Uso del método de la clase Tarea (OOP)
                print(f"Tarea '{descripcion}' marcada como completada.")
            else:
                print(f"No se encontró la tarea '{descripcion}'.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break  # Salir del bucle (paradigma imperativo)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_programa()