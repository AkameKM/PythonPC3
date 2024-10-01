############################# PROBLEMA 1 ############################
def get_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción (X/Y): ")
            
            x, y = fraccion.split('/')
            
            x = int(x)
            y = int(y)
            
            if y == 0:
                print("El denominador no puede ser 0.")
            if x > y:
                print("El numerador no puede ser mayor que el denominador.")
            
            porcentaje = (x / y) * 100
            
            if porcentaje <= 1:
                print("E")
            elif porcentaje >= 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")
        
        except ValueError:
            print("Error: Ingrese solo números enteros en el formato X/Y.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0.")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor, intente de nuevo.")


print(get_fraccion())
