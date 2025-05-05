class Matriz:
    def __init__(self, valores):
        if len(valores) != 2 or any(len(fila) != 2 for fila in valores):
            raise ValueError("La matriz debe ser de tamaño 2x2.")
        self.valores = valores

    def __add__(self, otra):
        resultado = [
            [self.valores[i][j] + otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __sub__(self, otra):
        resultado = [
            [self.valores[i][j] - otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __mul__(self, otra):
        resultado = [
            [
                self.valores[i][0] * otra.valores[0][j] + self.valores[i][1] * otra.valores[1][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Matriz(resultado)

    def mostrar(self):
        for fila in self.valores:
            print("[", "  ".join(f"{num:4}" for num in fila), "]")


def ingresar_matriz(nombre):
    print(f"\nIngrese los valores de la matriz {nombre} (2x2):")
    matriz = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"Ingrese el valor de {nombre.lower()}{i+1}{j+1}: "))
            fila.append(valor)
        matriz.append(fila)
    
    instancia = Matriz(matriz)
    print(f"\nMatriz {nombre} ingresada:")
    instancia.mostrar()
    return instancia


def menu():
    print("\n--- Calculadora de Matrices 2x2 ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")


def main():
    matriz1 = ingresar_matriz("A")
    matriz2 = ingresar_matriz("B")

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2", "3"]:
            print("\nMatriz A:")
            matriz1.mostrar()
            print("\nMatriz B:")
            matriz2.mostrar()

        if opcion == "1":
            resultado = matriz1 + matriz2
            print("\nResultado de la suma:")
            resultado.mostrar()
        elif opcion == "2":
            resultado = matriz1 - matriz2
            print("\nResultado de la resta:")
            resultado.mostrar()
        elif opcion == "3":
            resultado = matriz1 * matriz2
            print("4\nResultado de la multiplicación:")
            resultado.mostrar()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
