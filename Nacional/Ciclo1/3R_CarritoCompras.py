'''
Reto3: Tirilla de compra y Descuento
Realizado por: Jorge Giovanni Sanabria Torres

Input:              	           
    1&Chocolatinas Cohete&3&300
    1&Mora&1&1000
    1&Pan de Maiz&5&300
    2&1022734737
    1&Televisor&2&1500000
    1&Teatro en Casa&1&450000
    2&99999287
    3

Output:
    Centro Comercial Unaleño
    Compra más y Gasta Menos
    NIT: 899.999.063
    Cliente: 1022734737
    Art Cant Precio
    Chocolatinas Cohete x3 $900
    Mora x1 $1000
    Pan de Maiz x5 $1500
    Total: $3400
    En esta compra tu descuento fue $0
    Gracias por tu compra
    ---
    Centro Comercial Unaleño
    Compra más y Gasta Menos
    NIT: 899.999.063
    Cliente: 99999287
    Art Cant Precio
    Televisor x2 $3000000
    Teatro en Casa x1 $450000
    Total: $2760000
    En esta compra tu descuento fue $690000
    Gracias por tu compra
    ---
'''
import math

def read_articles():
    article = input('')
    return article.split('&')

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

def print_strip(article, total_buy, cc):
    strip = 'Centro Comercial Unaleño \n'\
        'Compra más y Gasta Menos \n'\
        'NIT: 899.999.063 \n'\
        f'Cliente: {cc} \n'\
        'Art Cant Precio \n'\
        f'{article}'\
        f'{get_discount(total_buy)}'\
        'Gracias por tu compra\n'\
        '---'    

    print(strip)

if __name__ == '__main__':
    article = ''
    total_buy = 0
    must_continue = True
    while must_continue:
        data = read_articles()

        if data[0] == '1':
            buy = int(data[2]) * int(data[3])
            article += f'{data[1]} x{data[2]} ${buy} \n'
            total_buy += buy
        elif data[0] == '2':
            print_strip(article, total_buy, data[1])
            article, total_buy = '', 0
        else:
            must_continue = False