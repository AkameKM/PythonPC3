# main.py
from gestion import gestion_biblioteca
from libro import Libro

def menu_biblioteca():
    print("\n¡ MENÚ DE LA BIBLIOTECA!")
    print("1. Agregar un libro")
    print("2. Listar los libros")
    print("3. Buscar un libro por título")
    print("4. Buscar un libro por autor")
    print("5. Salir")

def main():
    gestion = gestion_biblioteca()

    while True:
        menu_biblioteca()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            isbn = input("Ingresa el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == "2":
            gestion.listar_libros()

        elif opcion == "3":
            titulo = input("Ingresa el título del libro que deseas buscar: ")
            gestion.buscar_por_titulo(titulo)

        elif opcion == "4":
            autor = input("Ingresa el nombre del autor que deseas buscar: ")
            gestion.buscar_por_autor(autor)

        elif opcion == "5":
            print("¡SALIENDO DE LA BIBLIOTECA!")
            break

        else:
            print("SELECCIONE UNA OPCIÓN VALIDA.")

if __name__ == "__main__":
    main()
