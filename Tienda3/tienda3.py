import unittest

# Clase Producto para representar los productos de la tienda
class Producto:
    """Representa un producto en la tienda."""
  
    def __init__(self, nombre: str, precio: int, cantidad: int, descripcion: str, clasificacion: str):
        """Inicializa los atributos del producto con los valores proporcionados."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        """Devuelve una representación en cadena del producto para su visualización."""
        return f"|{self.nombre:<10}|{self.cantidad:>4} cantidad/und |{self.precio:>6} Precio/COP |{self.descripcion:<20}|{self.clasificacion:<12}|"

    def total_precio(self):
        """Calcula el precio total del producto (precio * cantidad) para el inventario."""
        return self.precio * self.cantidad

    def calcula_precio(self, cantidad):
        """Devuelve el precio total a pagar por una cantidad especificada de este producto."""
        return self.precio * cantidad

    def inventario_precio(self):
        """Devuelve el valor total de mercancía de este producto en el inventario (precio * cantidad)."""
        return self.total_precio()


def solicitar_producto(num):
    """Solicita los datos de un producto al usuario y devuelve un objeto Producto con la información ingresada."""
    nombre = input(f"¿Cuál es el nombre del Producto {num}?\n> ")
    precio = int(input(f"Precio de '{nombre}'?\n> "))
    cantidad = int(input(f"¿La cantidad de '{nombre}'?\n> "))
    descripcion = input(f"Introduzca la descripción de '{nombre}':\n> ")
    clasificacion = input(f"¿Qué clasificación tiene '{nombre}'?\n> ")
    # Retorna el objeto Producto con la información proporcionada
    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def run():
    """Función principal que ejecuta el flujo principal del programa, solicitando los productos y mostrando los resúmenes."""
    print("¡¡Bienvenido a su inventario de la tienda!!")
    
    # Solicita cuántos productos va a ingresar el usuario
    n = int(input("¿Cuántos productos va a ingresar? "))
    
    # Crear la lista de productos pidiendo la información de cada uno al usuario
    productos = [solicitar_producto(i) for i in range(1, n+1)]

    # Mostrar el resumen de los productos ingresados
    print("\nResumen de productos ingresados:")
    print("|Producto  |Cantidad   |Precio/Cop     |Descripción           |Clasificación |")
    print("|----------|------------|---------------|----------------------|--------------|")
    for producto in productos:
        print(producto)

    # Mostrar el precio a pagar por una cantidad de 5 unidades para cada producto
    print("\nPrecio a pagar por una cantidad de 5 por cada producto:")
    for producto in productos:
        print(f"{producto.nombre:<10} | Precio por 5 unidades: {producto.calcula_precio(5):<10} COP")

    # Mostrar el resumen de precios totales por clasificación
    resumen_por_clasificacion(productos)


def resumen_por_clasificacion(productos):
    """Muestra el resumen de precios por clasificación, agrupando los productos por su tipo."""
    clasificaciones = {}

    # Acumula los precios totales por clasificación
    for p in productos:
        if p.clasificacion not in clasificaciones:
            clasificaciones[p.clasificacion] = 0
        clasificaciones[p.clasificacion] += p.total_precio()

    # Muestra el resumen de precios totales por clasificación
    print("\nPrecios por clasificación:")
    print("|Clasificación  |Precio total     |")
    print("|---------------|-----------------|")
    for clasificacion, precio in clasificaciones.items():
        print(f"|{clasificacion:<15}|{precio:<16} COP |")


# Test unitario
class TestProducto(unittest.TestCase):
    """Prueba unitaria para verificar la correcta creación y funcionalidad de un Producto."""
    
    def test_creacion_producto(self):
        """Verifica que los atributos de un producto sean correctamente asignados."""
        producto = Producto("freson", 4000, 30, "Fresón de calidad", "alimentación")
        self.assertEqual(producto.nombre, "freson")
        self.assertEqual(producto.precio, 4000)
        self.assertEqual(producto.cantidad, 30)
        self.assertEqual(producto.descripcion, "Fresón de calidad")
        self.assertEqual(producto.clasificacion, "alimentación")

    def test_total_precio(self):
        """Verifica que el cálculo del precio total de inventario sea correcto."""
        producto = Producto("manzana", 1000, 50, "Manzanas rojas", "fruta")
        self.assertEqual(producto.total_precio(), 50000)  # 1000 * 50

    def test_calcula_precio(self):
        """Verifica que el cálculo del precio por una cantidad específica de unidades sea correcto."""
        producto = Producto("mango", 1500, 20, "Mango maduro", "fruta")
        self.assertEqual(producto.calcula_precio(5), 7500)  # 1500 * 5

    def test_inventario_precio(self):
        """Verifica que el cálculo del precio total del inventario sea correcto."""
        producto = Producto("banana", 1200, 30, "Bananas frescas", "fruta")
        self.assertEqual(producto.inventario_precio(), 36000)  # 1200 * 30


# Condicional para ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    run()  # Ejecuta la función principal para iniciar el programa
    unittest.main(exit=False)  # Ejecuta las pruebas unitarias sin detener el flujo del programa
