#Problema 6
#Descripción: Este programa calcula el interés compuesto dado un capital, tasa y tiempo.

CI = float(input("Ingrese el capital invertido: "))
TI = float(input("Ingrese la tasa de interés anual: "))
t = int(input("Ingrese el periodo de ahorro en años: "))

print("Interés compuesto = $", CI*(1 + TI)**t)