############################# PROBLEMA 7 ############################
import math

class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return f"Vector: ({otro_punto.x - self.x}, {otro_punto.y - self.y})"

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class rectangulo:
    def __init__(self, punto_inicial=punto(), punto_final=punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

A = punto(2, 3)
B = punto(5, 5)
C = punto(-3, -1)
D = punto(0, 0)

print(f"punto A: {A}")
print(f"punto B: {B}")
print(f"punto C: {C}")
print(f"punto D: {D}")

print(f"Cuadrante de A: {A.cuadrante()}")
print(f"Cuadrante de C: {C.cuadrante()}")
print(f"Cuadrante de D: {D.cuadrante()}")

print(f"Vector AB: {A.vector(B)}")
print(f"Vector BA: {B.vector(A)}")

rectangulo = rectangulo(A, B)
print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")
