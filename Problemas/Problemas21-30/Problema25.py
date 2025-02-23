#Problema 25
#Descripción: Este programa genera y analiza histogramas de datos.

import numpy as np
import matplotlib.pyplot as plt

# Función para generar datos aleatorios
def generar_datos(num_datos=100, distribucion='normal', parametros=None):
    if distribucion == 'normal':
        # Por defecto se generará una distribución normal con media=0 y desviación estándar=1
        mu, sigma = parametros if parametros else (0,1)
        datos = np.random.normal(mu, sigma, num_datos)
    elif distribucion == 'uniforme':
        # Por defecto se generará una distribución uniforme entre 0 y 1
        a, b = parametros if parametros else (0,1)
        datos = np.random.uniform(a, b, num_datos)
    else:
        raise ValueError("Distribución no soportada")
    return datos

# Función para analizar los datos
def analizar_datos(datos):
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    varianza = np.var(datos)
    return media, desviacion_estandar, varianza

# Función para graficar el histograma
def graficar_histograma(datos, bins=30, color='blue', titulo="Histograma de datos", xlabel="Valores",ylabel="Frecuencia"):
    plt.hist(datos, bins=bins, color=color, edgecolor='black', alpha=0.7)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Función principal para generar datos, analizarlos y graficar el histograma
def main():
    # Generar datos
    num_datos = 1000
    distribucion = 'normal' # Cambiar entre 'normal' y 'uniforme'
    parametros = (0,1) # Para 'normal' (mu, sigma) o para 'uniforme' (a,b)

    datos = generar_datos(num_datos, distribucion, parametros)

    # Analizar los datos
    media, desviacion_estandar, varianza = analizar_datos(datos)
    print(f"Estadísticas de los datos:")
    print(f"Media: {media}")
    print(f"Desviación Estándar: {desviacion_estandar}")
    print(f"Varianza: {varianza}")

    # Graficar el histograma
    graficar_histograma(datos, bins=30)

if __name__ == "__main__":
    main()

"""En este caso, se emplearon las bibliotecas 'numpy' y matplotlib para una mejor la eficiencia del programa,
utilizando 'numpy' como una manera de sustituir 'random' y 'math 'ya que la primera tiene una mejor flexibilidad
para el manejo de datos numéricos muy grandes; asimismo, se empleó 'matplotlib' ya posee la cualidad de permitir 
crear gráficos complejos."""