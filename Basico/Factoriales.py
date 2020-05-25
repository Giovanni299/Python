def getFactorial(num):
    '''Obtiene el factorial de un numero
        num: numero del que se quiere calcular el factorial
        return: calculo del factorial'''

    fact = 1
    for i in range(1, num+1):
        fact = fact * i

    return fact   

value = int(input('Factorial de: '))
result = getFactorial(value)
print(f'El factortial de {value } es {result}')
