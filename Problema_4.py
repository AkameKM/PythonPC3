############################# PROBLEMA 4 ############################

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    
    def calcular_area_rectangulo(self):
        return self.largo * self.ancho  

class CUADRADO(RECTANGULO):
    
    def __init__(self, lado):
        
        super().__init__(lado, lado)  

largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = RECTANGULO(largo_rectangulo, ancho_rectangulo)


lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
cuadrado = CUADRADO(lado_cuadrado)


print(f"El área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho} es: {rectangulo.calcular_area_rectangulo():.2f}")
print(f"El área del cuadrado con lado {cuadrado.largo} es: {cuadrado.calcular_area_rectangulo():.2f}")
