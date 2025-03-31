#  Ejercicio 6: Sistema de Gestión de Vehículos
"""Descripción: Este programa emplea una clase llamada 'Vehiculo' con los siguientes atributos y métodos:
 * Atributos: marca, modelo, año y precio.
 * Método para mostrar la información del vehículo.
 * Posee subclases llamadas 'Automovil' y 'Motocicleta' con atributos adicionales como número de puertas o cilindrada."""

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}"

# Subclase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, numero_puertas):
        super().__init__(marca, modelo, año, precio)
        self.numero_puertas = numero_puertas

    def mostrar_info(self):
        info_vehiculo = super().mostrar_info()
        return f"{info_vehiculo}, Número de puertas: {self.numero_puertas}"

# Subclase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        info_vehiculo = super().mostrar_info()
        return f"{info_vehiculo}, Cilindrada: {self.cilindrada}cc"

# Ejemplo de uso:
auto = Automovil("Toyota", "Corolla", 2021, 20000, 4)
moto = Motocicleta("Honda", "CBR500R", 2020, 7000, 500)

print(auto.mostrar_info())
print(moto.mostrar_info())