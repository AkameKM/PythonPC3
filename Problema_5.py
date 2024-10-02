############################# PROBLEMA 5 ############################
class Alumno:
    
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None  
        self.nota = None
    
    def display(self):
        print(f"El nombre del alumno es: {self.nombre}")
        print(f"El número de registro del alumno es: {self.num_registro}")
        if self.edad is not None: 
            print(f"La edad del estudiante es: {self.edad}")
        else:
            print("Edad: No asignada")
        
        if self.nota is not None:
            print(f"La nota del estudiante es: {self.nota}")
        else:
            print("Nota: No asignada")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.nota = nota

nombre = input("Ingrese el nombre del alumno: ")
num_registro = input("Ingrese el número de registro del alumno: ")

alumno_1 = Alumno(nombre, num_registro)

edad_alumno = int(input("Ingrese la edad del alumno: "))
alumno_1.setAge(edad_alumno)

nota_alumno = float(input("Ingrese la nota del alumno: "))
alumno_1.setNota(nota_alumno)


alumno_1.display()
