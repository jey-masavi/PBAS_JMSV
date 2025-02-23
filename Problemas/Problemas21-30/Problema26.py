#Problema 26
#Descripción: Este programa implementa una agenda de contactos.

agenda = {}

def mostrar_contactos():
    print("\nNombre: ".ljust(20) + "Identificador: ".ljust(20) + "Teléfono: ")
    print("-" * 55)
    for nombre, datos in agenda.items():
        print(f"{nombre.ljust(20)} {datos['id'].ljust(20)} {datos['tel']}")

def main():
    while True:
        print("\nOPCIONES:")
        print("1. Añadir nuevo contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = int(input("Introduzca el número de la opción a elegir: "))

        if opcion == 1:
            nombre = input("Nombre del contacto: ")
            id = input("Identificador del contacto: ")
            tel = input("Teléfono del contacto: ")
            agenda[nombre] = {'id': id, 'tel': tel}
            print("El contacto ha sido añadido")
    
        elif opcion == 2:
            nombre_buscar = input("Nombre del contacto a buscar: ")
            if nombre_buscar in agenda:
                print(f"Su identificador y teléfono son {agenda[nombre_buscar]}")
            else:
                print("No se encontró el contacto.")
    
        elif opcion == 3:
            if not agenda:
                print("La agenda está vacía.")
            else:
                mostrar_contactos()
        elif opcion == 4:
            nombre_eliminar = input("Nombre del contacto a eliminar: ")
            if nombre_eliminar in agenda:
                agenda.pop(nombre_eliminar)
                print("El contacto ha sido eliminado.")
            else:
                print("No se encontró el contacto.")
        elif opcion == 5:
            print("Saliendo de la agenda de contactos...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()