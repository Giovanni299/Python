'''
Practica1: Banco Unaleño
Realizado por: Jorge Giovanni Sanabria Torres

Input:
Cantidad de dinero

10.000, $20.000, $50.000 y $100.000
'''

valor = int(input('Valor a retirar: '))
print(valor//100000,'x $100000')
valor = valor % 100000
print(str(valor//50000) ,'x $50000')
valor = valor % 50000
print(str(valor//20000) ,'x $20000')
valor = valor % 20000
print(str(valor//10000) ,'x $10000')
valor = valor % 10000    