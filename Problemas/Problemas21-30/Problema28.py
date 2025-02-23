#Problema 28
#Descripción: Este programa simula una cuenta bancaria con depósitos y retiros.

saldo = 0

# Función para mostrar el saldo actual
def mostrar_saldo(saldo):
    print(f"El saldo actual de tu cuenta bancaria: ${saldo:.2f}")
    return saldo

# Función para hacer un depósito
def depositar(saldo):
    monto = float(input("¿Cuánto desea depositar? $"))
    if monto > 0:
        saldo += monto
        print(f"Depósito exitoso. Ha depositado: ${monto:.2f}")
    else:
        print("El monto debe ser positivo para realizar el depósito.")
    return saldo

# Función para hacer un retiro
def retirar(saldo):
    monto = float(input("¿Cuánto desea retirar? $"))
    if monto > 0:
        if monto <= saldo:
            saldo -= monto
            print(f"Retiro exitoso. Ha retirado: ${monto:.2f}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    else:
        print("El monto debe ser positivo para realizar el retiro.")
    return saldo

# Función que muestra el menú de opciones
def menu():
    print("\n¡Bienvenido a su cuenta bancaria!")
    print("1. Mostrar saldo")
    print("2. Hacer un depósito")
    print("3. Hacer un retiro")
    print("4. Salir")

# Función principal que ejecuta el programa
def main():
    saldo = 0
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            saldo = mostrar_saldo(saldo)
        
        elif opcion == 2:
            saldo = depositar(saldo)

        elif opcion == 3:
            saldo = retirar(saldo)
        
        elif opcion == 4:
            print("¡Gracias por usar nuestros servicios! \nSaliendo...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()