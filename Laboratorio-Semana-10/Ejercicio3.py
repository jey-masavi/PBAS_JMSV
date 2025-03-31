# Ejercicio 3: Gestión de Contactos con Tuplas y Estructuras Anidadas
""" Descripción: Este programa permite gestionar contactos de la siguiente manera:
 * Cada contacto se almacena como una tupla con nombre, número y correo.
 * La agenda de contactos se almacena en una lista.
 * Permite agregar nuevos contactos.
 * Busca contactos por nombre e imprime sus detalles.
 * Lista todos los contactos en orden alfabético"""

# Definir la agenda de contactos como una lista
agenda = []

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    correo = input("Ingrese el correo electrónico del contacto: ")

    # Tupla con los datos del contacto
    contacto = (nombre, numero, correo)

    # Añadir el contacto a la agenda
    agenda.append(contacto)
    print(f"Contacto {nombre} agregado exitosamente.")

# Función para buscar un contacto por nombre
def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto que desea a buscar: ")
    encontrado = False

    for contacto in agenda:
        if contacto[0].lower() == nombre_buscar.lower():
            print(f"Nombre: {contacto[0]}")
            print(f"Número: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.")

# Función para listar todos los contacto en orden alfabético
def listar_contactos():
    if not agenda:
        print("No hay contactos en la agenda.")
        return
    
    # Ordenar la agenda alfabéticamente por el nombre del contacto
    agenda_ordenada = sorted(agenda, key = lambda x: x[0].lower())

    print("Lista de contactos en orden alfabético:")
    for contacto in agenda_ordenada:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

# Función para mostrar el menú y manejar las opciones
def menu():
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar un nuevo contacto")
        print("2. Buscar contacto por nombre")
        print("3. Listar todos los contactos")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            listar_contactos()
        elif opcion == '4':
            print("Saliendo de la agenda de contactos... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

# Ejecutar el programa
menu()