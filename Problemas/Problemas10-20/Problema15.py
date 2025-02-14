#Problema 15
#Descripción: Este programa determina si un año es bisiesto.

year = int(input("Ingrese un año: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("El año ", year, " es bisiesto")
else:
    print("El año ", year, " no es bisiesto")