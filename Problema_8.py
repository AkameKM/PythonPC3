############################# PROBLEMA 6 ############################

import operaciones
a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))

operacion_de_suma = operaciones.suma(a, b)
print(f"Suma: {operacion_de_suma}")

operacion_de_resta = operaciones.resta(a, b)
print(f"Resta: {operacion_de_resta}")

operacion_de_multiplicacion = operaciones.multiplicacion(a, b)
print(f"Producto: {operacion_de_multiplicacion}")

operacion_de_division = operaciones.division(a, b)
print(f"División: {operacion_de_division}")


