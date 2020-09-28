'''
Practica1: Carrito
Realizado por: Jorge Giovanni Sanabria Torres

Input:              	           
1
2
3
6
7
10	

Output:
suma total = 488.0973053848792
'''
import math

def areaCircle(radio):
    return math.pi * radio**2

def areaSquare(sideA, sideB):
    return sideA*sideB

val = []
for i in range(6):
    val.append(int(input()))

print('suma total =', areaSquare(val[0], val[1]) + areaSquare(val[2], val[3]) + areaCircle(val[4]) + areaCircle(val[5]))
