############################# PROBLEMA 2 ############################

def lista_calificaciones():
    while True:
        try:
            lista = input("Ingrese la lista de calificaciones separadas por comas: ")
            
            calificaciones = lista.split(',')
            
            calificaciones_con_comas = [int(calificacion.strip()) for calificacion in calificaciones]
            
            return calificaciones_con_comas
        
        except ValueError:
        
            print("ERROR: TODAS LAS CALIFICACIONES DEBEN SER NÚMEROS ENTEROS Y DEBEN ESTAR SEPARADOS POR COMAS")

calificaciones = lista_calificaciones()
print("Lista de calificaciones ingresadas:", calificaciones)
