class rectangulo():
    def __init__(self, alto, ancho):
        ''' Constructor '''
        self._alto = alto
        self._ancho = ancho

    def area(self):
        return self._alto * self._ancho

class cuadrado(rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rect = rectangulo(5, 3)
    print(f'Area del rectangulo: {rect.area()}')

    cuad = cuadrado(5)
    print(f'Area del cuadrado: {cuad.area()}')