from datetime import datetime


class Producto:
    """
    Clase para representar un producto de tienda con sus datos básicos.
    """

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        # Guardamos todos los datos del producto cuando se crea
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        self.descripcion = descripcion
        self.clasificacion = clasificacion
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mostrar_info(self):
        # Devolvemos los datos del producto bien organizados en una sola línea
        return (
            f"|{self.nombre:<15} |{self.precio:<10.2f} |{self.cantidad:<8} "
            f"|{self.descripcion:<30} |{self.clasificacion:<15} |{self.fecha_ingreso} |"
        )


def ingresar_productos():
    """
    Esta función se encarga de pedirle al usuario cuántos productos quiere ingresar
    y luego recopila los datos de cada uno.
    """
    productos = []
    cantidad = int(input("¿Cuántos productos deseas ingresar?\n> "))

    for i in range(cantidad):
        print(f"\nProducto #{i + 1}")
        nombre = input("→ Nombre: ").strip()
        precio = input("→ Precio (ej: 2500): ").strip()
        cantidad_prod = input("→ Cantidad: ").strip()
        descripcion = input("→ Descripción (breve): ").strip()
        clasificacion = input("→ Clasificación (ej: alimentos, aseo, etc): ").strip()

        # Creamos un objeto Producto con los datos ingresados
        producto = Producto(nombre, precio, cantidad_prod, descripcion, clasificacion)
        productos.append(producto)

    return productos


def mostrar_resumen_productos(productos):
    """
    Muestra todos los productos ingresados en forma de tabla.
    """
    print("\n📦 Lista de productos en inventario:")
    print("|Nombre          |Precio     |Cantidad |Descripción                   "
          "|Clasificación     |Fecha de ingreso           |")
    print("|--------------- |---------- |-------- |------------------------------"
          "|------------------|---------------------------|")

    for producto in productos:
        print(producto.mostrar_info())


def calcular_total_por_clasificacion(productos):
    """
    Agrupa los productos por su clasificación y suma el valor total de cada grupo.
    """
    resumen = {}

    for producto in productos:
        total = producto.precio * producto.cantidad

        if producto.clasificacion in resumen:
            resumen[producto.clasificacion] += total
        else:
            resumen[producto.clasificacion] = total

    print("\n🧾 Total por clasificación:")
    for clasificacion, total in resumen.items():
        print(f"- {clasificacion:<15}: ${total:,.2f}")


def main():
    """
    Aquí es donde se ejecuta todo el programa.
    """
    productos = ingresar_productos()
    mostrar_resumen_productos(productos)
    calcular_total_por_clasificacion(productos)


def test_producto():
    """
    Prueba rápida para comprobar que la clase Producto guarda bien los datos.
    """
    p = Producto("Leche", 3000, 2, "Entera en bolsa", "alimentos")
    assert p.nombre == "Leche"
    assert p.precio == 3000
    assert p.cantidad == 2
    assert p.descripcion == "Entera en bolsa"
    assert p.clasificacion == "alimentos"
    print(" Test de clase Producto: OK")


if __name__ == "__main__":
    test_producto()  # Primero probamos que la clase funcione bien
    main()           # Luego corremos el programa
