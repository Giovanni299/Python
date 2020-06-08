import random

def busquedad_lineal(lista, objetivo):
    for i in lista:
        if i == objetivo:
            return True
    
    return False


if __name__ == "__main__":
    tamaño = int(input('Ingrese el tamaño de la lista: '))
    objetivo_inp = int(input('Ingrese el numero a buscar: '))

    lista = [random.randint(0, 100) for i in range(tamaño)]
    match = busquedad_lineal(lista, objetivo_inp)

    print(lista)
    print(f'El numero {objetivo_inp} {"fue" if match else "no fue"} encontrado en la lista')
