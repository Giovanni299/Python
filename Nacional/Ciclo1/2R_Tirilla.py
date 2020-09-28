'''
Reto2: Tirilla de compra y Descuento
Realizado por: Jorge Giovanni Sanabria Torres

Input:              	           
    3
    Chocolatinas Cohete
    300
    Mora
    1000
    Pan de Maiz
    300	

Output:
    Centro Comercial Unaleño
    Compra más y Gasta Menos
    NIT: 899.999.063
    Chocolatinas Cohete $300
    Mora $1000
    Pan de Maiz $300
    Total: $1600
    En esta compra tu descuento fue $0
    Gracias por tu compra
'''
import math

def read_articles():
    num_articles = int(input('Numero de articulos: '))
    strip = 'Centro Comercial Unaleño \n'\
        'Compra más y Gasta Menos \n'\
        'NIT: 899.999.063 \n'

    total_buy = 0
    for i in range(num_articles):
        name = input(f'Nombre del articulo {i}: ')
        value = input('Precio: ')
        strip += f'{name} ${value}\n'
        total_buy += int(value)
    
    strip += get_discount(total_buy)
    strip += 'Gracias por tu compra'

    return strip

def get_discount(total_buy):
    discount = 0
    if total_buy > 150000 and total_buy <= 300000:
        discount = total_buy * 0.1
    elif total_buy > 300000 and total_buy <= 700000:
        discount = total_buy * 0.15
    elif total_buy > 700000:
        discount = total_buy * 0.2
        
    strip = f'Total: ${math.ceil(total_buy-discount)}\n'
    strip += f'En esta compra tu descuento fue ${int(discount)}\n'
    return strip

if __name__ == '__main__':
    print(read_articles())