########################### gestion.py ################################
from libro import Libro

class gestion_biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        if not self.libros:
            print("¡NO HAY LIBROS EN LA BIBLIOTECA!.")
        else:
            for libro in self.libros:
                print(libro)

    def buscar_por_titulo(self, titulo):
        resultado_busqueda = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if resultado_busqueda:
            for libro in resultado_busqueda:
                print(libro)
        else:
            print(f"NO SE ENCONTRÓ NINGÚN LIBRO CON ESE TÍTULO: {titulo}")

    def buscar_por_autor(self, autor):
        resultado_busqueda = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if resultado_busqueda:
            for libro in resultado_busqueda:
                print(libro)
        else:
            print(f"NO SE ENCONTRÓ NINGÚN LIBRO DEL AUTOR: {autor}")
