############################# PROBLEMA 9 ############################
from Problema_3 import CIRCULO
from Problema_4 import RECTANGULO, CUADRADO

def validar_numeros_correctos(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("¡ERROR: DEBE SER UN NÚMERO POSITIVO!")
        except ValueError:
            print("¡ERROR: ENTRADA INVÁLIDA. INGRESE UN NÚMERO ENTERO!")

def menu():
    while True:
        print("\nBIENVENIDO AL MENÚ DE OPCIONES: SELECCIONE UNA OPCIÓN:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        print(opcion)
        
        if opcion == "1":
            radio = validar_numeros_correctos("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"Área del círculo: {circulo.calcular_area()}")

        elif opcion == "2":
            largo = validar_numeros_correctos("Ingrese el largo del rectángulo: ")
            ancho = validar_numeros_correctos("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"Área del rectángulo: {rectangulo.calcular_area_rectangulo()}")

        elif opcion == "3":
            lado = validar_numeros_correctos("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"Área del cuadrado: {cuadrado.calcular_area_rectangulo()}")

        elif opcion == "4":
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida, por favor seleccione una opción válida.")

menu()
