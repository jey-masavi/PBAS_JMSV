# Ejercicio 2: Manejo de inventario con listas y diccionarios.
"""Descripción: Este programa es un sistema de inventario con las siguientes funcionalidades:
 * Permite al usuario agregar productos, especificando nombre, categoría, precio y cantidad.
 * Permite la eliminación de productos por su nombre.
 * Busca productos por nombre y muestra su información.
 * Muestra todos los productos ordenados por precio de menor a mayor."""

# Sistema de inventario
inventario = []

# Función para agregar productos
def agregar_producto(nombre, categoria, precio, cantidad):
    producto = {
        'nombre': nombre,
        'categoria': categoria,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

# Función para eliminar productos por nombre
def eliminar_producto(nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")

# Función para buscar productos por nombre
def buscar_producto(nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            print(f"Producto encontrado: {producto}")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")

# Función para mostrar productos ordenados por precio
def mostrar_productos_ordenados():
    # Ordenar los productos por precio (de menor a mayor)
    productos_ordenados = sorted(inventario, key = lambda x: x['precio'])
    print("Productos ordenados por precio:")
    for producto in productos_ordenados:
        print(f"{producto['nombre']} - {producto['categoria']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")

# Menú interactivo
def menu():
    while True:
        print("\nSistema de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos ordenados por precio")
        print("5. Salir")

        opcion = input("Elija una opción: ")
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            agregar_producto(nombre, categoria, precio, cantidad)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(nombre)

        elif opcion == '4':
            mostrar_productos_ordenados()

        elif opcion == '5':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()