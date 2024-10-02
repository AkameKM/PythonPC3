############################# PROBLEMA 6 ############################
class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def informacion(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Año: {self.año}")

class Catalogo:
    def __init__(self):
        self.productos = []

    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al catálogo.")

   
    def revisar_catalogo(self):
        if len(self.productos) == 0:
            print("El catálogo está vacío.")
        else:
            print("Productos en el catálogo:")
            for producto in self.productos:
                producto.informacion()

    def filtrar_por_año(self, año):
        print(f"\nProductos del año {año}:")
        productos_filtrados = [prod for prod in self.productos if prod.año == año]
        if productos_filtrados:
            for producto in productos_filtrados:
                producto.informacion()
        else:
            print(f"No se encontraron productos del año {año}.")

    def filtrar_producto_por_precio(self, precio):
        print(f"\nProductos con precio ${precio}:")
        productos_filtrados = [prod for prod in self.productos if prod.precio == precio]
        if productos_filtrados:
            for producto in productos_filtrados:
                producto.informacion()
        else:
            print(f"No se encontraron productos con este precio ${precio}.")


producto_1 = input("Ingrese el nombre del primer producto: ")
precio_1 = float(input("Ingrese el precio del primer producto: "))
año_1 = int(input("Ingrese el año del primer producto: "))

producto_2 = input("Ingrese el nombre del segundo producto: ")
precio_2 = float(input("Ingrese el precio del segundo producto: "))
año_2 = int(input("Ingrese el año del segundo producto: "))

producto_3 = input("Ingrese el nombre del tercer producto: ")
precio_3 = float(input("Ingrese el precio del tercer producto: "))
año_3 = int(input("Ingrese el año del tercer producto: "))

producto1 = Producto(producto_1, precio_1, año_1)
producto_2 = Producto(producto_2, precio_2, año_2)
producto_3 = Producto(producto_3, precio_3, año_3)


catalogo = Catalogo()

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto_2)
catalogo.agregar_producto(producto_3)

catalogo.revisar_catalogo()

# Ejemplos de las funciones Filtrar producto por año y por precio

catalogo.filtrar_por_año(2024)

catalogo.filtrar_producto_por_precio(90)
