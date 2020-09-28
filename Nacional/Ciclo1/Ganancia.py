'''
Reto1: Calculo de ganancia
Realizado por: Jorge Giovanni Sanabria Torres

Input:
Chocolatinas Cohete
300
550
1000
'''

producto = input('Ingrese el nombre del producto: ')
cu = input('Ingrese el costo unitario: ')
pvp = input('Ingrese el precio de venta al publico: ')
unidades = input('Ingrese la cantidad de unidades disponibles: ')

print('Producto:', producto)
print('CU: $' + cu)
print('PVP: $' + pvp)
print('Unidades Disponibles:', unidades)
print('Ganancia:', int(unidades) * (int(pvp) - int(cu)))