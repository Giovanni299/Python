class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'{self.nombre} va caminando')

class Ciclista(Persona):
    def __init__(self, name):
        super().__init__(name)

    def avanza(self):
        print(f'{self.nombre} va en bicicleta')

if __name__ == "__main__":
    ciclista = Ciclista('Gio')
    ciclista.avanza()