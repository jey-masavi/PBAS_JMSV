#Problema 30
#Descripción: Este programa implementa funciones recursivas.

print("POTENCIA DE UN NÚMERO (x^n)")
# Función recursiva para calcular la potencia
def potencia(base, exponente):
    # Caso base: cualquier número elevado a la potencia de 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base^exponente = base * base^(exponente - 1)
    else:
        return base * potencia(base, exponente - 1)
    
# Función principal para ejecutar el programa
def main():
    base = int(input("Introduzca la base: "))
    exponente = int(input("Introduzca el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es : {resultado}")

if __name__ == "__main__":
    main()