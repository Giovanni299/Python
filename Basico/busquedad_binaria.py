import random

def busquedad_binaria(lista, objetivo, inicio, fin):
    if inicio > objetivo or inicio >= fin:
        return False
    
    medio = (fin + inicio)//2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busquedad_binaria(lista, objetivo, medio + 1, fin)
    else:
        return busquedad_binaria(lista, objetivo, inicio, medio - 1)
    

if __name__ == "__main__":
    tamaño = int(input('Ingrese el tamaño de la lista: '))
    objetivo_inp = int(input('Ingrese el numero a buscar: '))

    lista = sorted([random.randint(0, 100) for i in range(tamaño)])
    match = busquedad_binaria(lista, objetivo_inp, 0, len(lista))

    print(lista)
    print(f'El numero {objetivo_inp} {"fue" if match else "no fue"} encontrado en la lista')