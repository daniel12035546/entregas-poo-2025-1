import unittest

class Producto:
  
    """Esta es la clase que va a represenyar el producto de la tienda"""

    def __init__(self, nombre: str, precio: int, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"|{self.nombre:<10}|{self.cantidad:>4} cantidad/und |{self.precio:>6} Precio/COP |"


def solicitar_producto(num):
  
    """En esta seccion solicitamos los dastos del producto"""
    nombre = input(f"¿Cual es el nombre del Producto {num}\n> ")
    precio = int(input(f"Precio de '{nombre}'?\n> "))
    cantidad = int(input(f"¿La cantidad de '{nombre}'?\n> "))
    return Producto(nombre, precio, cantidad)


def run():
    """Script entrypoint"""
    print("¡¡Bienvenido a su  inventario de la tienda!!")
    productos = [solicitar_producto(i) for i in range(1, 4)]

    print("\nResumen:")
    print("|Producto  |Cantidad   |Precio/Cop     |")
    print("|----------|------------|-----------|")
    for producto in productos:
        print(producto)


# Test unitario
class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        producto = Producto("freson", 4000, 30)
        self.assertEqual(producto.nombre, "freson")
        self.assertEqual(producto.precio, 4000)
        self.assertEqual(producto.cantidad, 30)


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
    unittest.main(exit=False)
