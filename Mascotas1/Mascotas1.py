from datetime import datetime


class Producto:
    """
    Esta clase representa un producto que se puede guardar en el inventario.
    """

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """
        Aquí se guardan todos los datos del producto cuando se crea.
        """
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mostrar_info(self):
        """
        Devuelve un texto con todos los datos del producto en una sola línea, bien ordenado.
        """
        return (
            f"|{self.nombre:<15} |{self.precio:<10.2f} |{self.cantidad:<8} "
            f"|{self.descripcion:<30} |{self.clasificacion:<15} |{self.fecha_ingreso} |"
        )


def ingresar_productos():
    """
    Esta función pregunta al usuario cuántos productos quiere ingresar y luego pide los datos de cada uno.
    """
    productos = []
    cantidad = int(input("¿Cuántos productos va a ingresar?\n> "))

    for i in range(cantidad):
        print(f"\nProducto {i+1}")
        nombre = input("> Nombre del producto:\n< ").strip()
        precio = input("> Precio del producto:\n< ").strip()
        cantidad_prod = input("> Cantidad en inventario:\n< ").strip()
        descripcion = input("> Descripción del producto:\n< ").strip()
        clasificacion = input("> Clasificación (ej: alimentos, aseo, licor):\n< ").strip()

        # Creamos el objeto producto con los datos que ingresó el usuario
        producto = Producto(nombre, precio, cantidad_prod, descripcion, clasificacion)
        productos.append(producto)

    return productos


def mostrar_resumen_productos(productos):
    """
    Esta función muestra en pantalla todos los productos ingresados, uno por uno.
    """
    print("\nResumen de productos:")
    print("|Nombre          |Precio     |Cantidad |Descripción                   "
          "|Clasificación     |Fecha de ingreso           |")
    print("|--------------- |---------- |-------- |------------------------------"
          "|------------------|---------------------------|")
    for producto in productos:
        print(producto.mostrar_info())


def calcular_total_por_clasificacion(productos):
    """
    Aquí se calcula cuánto valen todos los productos por cada clasificación.
    Ej: cuánto valen todos los productos de aseo juntos, o todos los de alimentos.
    """
    resumen_clasificacion = {}

    for producto in productos:
        total = producto.precio * producto.cantidad

        if producto.clasificacion in resumen_clasificacion:
            resumen_clasificacion[producto.clasificacion] += total
        else:
            resumen_clasificacion[producto.clasificacion] = total

    print("\nResumen del precio total por clasificación:")
    for clasificacion, total in resumen_clasificacion.items():
        print(f"- {clasificacion:<15}: ${total:,.2f}")


def main():
    """
    Esta es la función principal. Aquí se juntan todas las partes del programa.
    """
    productos = ingresar_productos()
    mostrar_resumen_productos(productos)
    calcular_total_por_clasificacion(productos)


# Prueba rápida para asegurarnos de que la clase Producto funciona como debería
def test_producto():
    """
    Test sencillo para comprobar que la clase Producto guarda bien los datos.
    """
    p = Producto("Jabón", 2500, 4, "Para manos", "aseo")
    assert p.nombre == "Jabón"
    assert p.precio == 2500
    assert p.cantidad == 4
    assert p.descripcion == "Para manos"
    assert p.clasificacion == "aseo"
    print(" Test de producto OK")


if __name__ == "__main__":
    test_producto()  # Ejecuta el test antes de empezar
    main()           # Inicia el programa normal
