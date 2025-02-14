#Problema 13
#Descripción: Este programa convierte una temperarura entre distintas escalas.

def conversor_temp(valor, escala_origen):

    #Dicccionario de conversiones.
    conversiones = {
        '1': { 
            'F': (valor * 9/5) +32,
            'K': valor + 273.15,
            'Ra': (valor + 273.15) * 9/5,
            'Re': valor * 4/5
        },
        '2': {
            'C': (valor - 32) * 5/9,
            'K': (valor - 32) * 5/9 + 273.15,
            'Ra': valor + 459.67,
            'Re': (valor - 32) * 4/9
        },
        '3': {
            'C': valor - 273.15,
            'F': (valor - 273.15) * 9/5 + 32,
            'Ra': valor * 9/5,
            'Re': (valor - 273.15) * 4/5
        },
        '4': {
            'C': (valor - 491.67) * 5/9,
            'F': valor - 497.67,
            'K': valor * 5/9,
            'Re': (valor - 491.67) * 4/9
        },
        '5': {
            'C': valor * 5/4,
            'F': (valor * 9/4) + 32,
            'K': (valor * 5/4) + 273.15,
            'Ra': (valor * 9/4) + 491.67
        }
    }
    return conversiones[escala_origen]

def mostrar_resultados(temp_convertida, escala_origen):
    escalas = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine', 'Réaumur']

    nombres_escalas = {
        '1': 'Celsius',
        '2': 'Fahrenheit',
        '3': 'Kelvin',
        '4': 'Rankine',
        '5': 'Réaumur'
    }

    print(f"\nConversión desde {nombres_escalas[escala_origen]}:")
    for escala, temp in temp_convertida.items():
        print(f"{escala.capitalize()}: {temp:.2f}")

def main():
    print("Conversor de temperaturas entre escalas (Celsius, Fahrenheit, Kelvin, Rankine, Réaumur)\n")

    escala = input("Ingrese la escala de origen (1. Celsius, 2. Fahrenheit, 3. Kelvin, 4. Rankine, 5. Réaumur): ")
    valor = float(input("Ingrese los grados que desea convertir: "))

    if escala not in ['1', '2', '3', '4', '5']:
        print("Escala no válida. Por favor elija las disponibles (1. Celsius, 2. Fahrenheit, 3. Kelvin, 4. Rankine, 5. Réaumur): ")
        return
    temp_convertida = conversor_temp(valor, escala)
    mostrar_resultados(temp_convertida, escala)

if __name__ == "__main__":
    main()