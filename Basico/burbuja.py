import random

def orderList(listToOrder, len_list):
    for i in range(len_list):
        if listToOrder[i] > listToOrder[i+1]:
            listToOrder[i], listToOrder[i+1] = listToOrder[i+1], listToOrder[i]

    if len_list - 1 == 0:
        print(f'Lista ordenada: {listToOrder}')
        return

    orderList(listToOrder, len_list - 1)

if __name__ == "__main__":
   len_list = int(input('Tamaño de la lista: '))
   number_list = [random.randint(0, 99) for i in range(len_list)]
   print(f'Lista original: {number_list}')
   orderList(number_list, len_list - 1)
