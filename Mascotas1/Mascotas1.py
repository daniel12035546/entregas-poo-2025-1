from datetime import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mostrar_info(self):
        clase = "Perro" if isinstance(self, Perro) else "Gato"
        return f"|{clase:<6} |{self.nombre:<8} |{self.edad:<5} años |{self.raza:<12} |{self.fecha_ingreso} |"

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

class Gato(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)

mascotas = []

cantidad = int(input("¿Cuántas mascotas va a ingresar?\n> "))

for i in range(cantidad):
    print(f"Mascota {i+1}, ¿qué clase es (P)erro o (G)ato?")
    clase = input("< ").strip().lower()

    while clase not in ('p', 'g'):
        print("Opción inválida. Ingrese 'P' para Perro o 'G' para Gato.")
        clase = input("< ").strip().lower()

    es_perro = clase == 'p'
    tipo = "Perro" if es_perro else "Gato"

    nombre = input(f"> ¿Cuál es el nombre del {tipo}?\n< ").strip()
    edad = input(f"> ¿Qué edad tiene '{nombre}'?\n< ").strip()
    raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()

    mascota = Perro(nombre, edad, raza) if es_perro else Gato(nombre, edad, raza)
    mascotas.append(mascota)

print("\nResumen:")
print("|Clase  |Nombre   |Edad  |Raza         |Fecha de ingreso            |")
print("|------ |-------- |----- |------------ |----------------------------|")
for mascota in mascotas:
    print(mascota.mostrar_info())
