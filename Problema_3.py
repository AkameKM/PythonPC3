############################# PROBLEMA 3 ############################
import math  

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2  

radio_1= float(input("Ingrese el radio del primer círculo: "))
circulo_1 = CIRCULO(radio_1)  

radio_2= float(input("Ingrese el radio del segundo círculo: "))
circulo_2 = CIRCULO(radio_2)  

print(f"El área del primer círculo con radio {circulo_1.radio} es: {circulo_1.calcular_area():.2f}")
print(f"El área del segundo círculo con radio {circulo_2.radio} es: {circulo_2.calcular_area():.2f}")
