import unittest

# Clase Producto para representar los productos de la tienda
class Producto:
    """Representa un producto en la tienda."""
  
    def __init__(self, nombre: str, precio: int, cantidad: int, descripcion: str, clasificacion: str):
        """Inicializa los atributos del producto."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"|{self.nombre:<10}|{self.cantidad:>4} cantidad/und |{self.precio:>6} Precio/COP |{self.descripcion:<20}|{self.clasificacion:<12}|"

    def total_precio(self):
        """Calcula el precio total del producto (precio * cantidad)."""
        return self.precio * self.cantidad


def solicitar_producto(num):
    """Solicita los datos de un producto al usuario y devuelve un objeto Producto."""
    nombre = input(f"¿Cuál es el nombre del Producto {num}?\n> ")
    precio = int(input(f"Precio de '{nombre}'?\n> "))
    cantidad = int(input(f"¿La cantidad de '{nombre}'?\n> "))
    descripcion = input(f"Introduzca la descripción de '{nombre}':\n> ")
    clasificacion = input(f"¿Qué clasificación tiene '{nombre}'?\n> ")
    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def run():
    """Función principal que ejecuta el programa."""
    print("¡¡Bienvenido a su inventario de la tienda!!")
    n = int(input("¿Cuántos productos va a ingresar? "))
    
    # Crear la lista de productos
    productos = [solicitar_producto(i) for i in range(1, n+1)]

    # Mostrar resumen de productos
    print("\nResumen de productos ingresados:")
    print("|Producto  |Cantidad   |Precio/Cop     |Descripción           |Clasificación |")
    print("|----------|------------|---------------|----------------------|--------------|")
    for producto in productos:
        print(producto)

    # Mostrar resumen por clasificación
    resumen_por_clasificacion(productos)


def resumen_por_clasificacion(productos):
    """Muestra el resumen de precios por clasificación."""
    clasificaciones = {}

    # Acumula los precios totales por clasificación
    for p in productos:
        if p.clasificacion not in clasificaciones:
            clasificaciones[p.clasificacion] = 0
        clasificaciones[p.clasificacion] += p.total_precio()

    # Muestra el resumen
    print("\nPrecios por clasificación:")
    print("|Clasificación  |Precio total     |")
    print("|---------------|-----------------|")
    for clasificacion, precio in clasificaciones.items():
        print(f"|{clasificacion:<15}|{precio:<16} COP |")


# Test unitario
class TestProducto(unittest.TestCase):
    """Prueba unitaria para verificar la correcta creación de un Producto."""
    
    def test_creacion_producto(self):
        producto = Producto("freson", 4000, 30, "Fresón de calidad", "alimentación")
        self.assertEqual(producto.nombre, "freson")
        self.assertEqual(producto.precio, 4000)
        self.assertEqual(producto.cantidad, 30)
        self.assertEqual(producto.descripcion, "Fresón de calidad")
        self.assertEqual(producto.clasificacion, "alimentación")


# Condicional para ejecutar el programa solo si se ejecuta directamente
if __name__ == "__main__":
    run()  # Ejecuta la función principal
    unittest.main(exit=False)  # Ejecuta las pruebas unitarias sin salir del programa
