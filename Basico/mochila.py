
iteracion = 0

def morral(tamano_morral, pesos, valores, n):
    global iteracion

    iteracion += 1
    print(f'Iteración {iteracion} probando con n={n}')

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)

    return max(valores[n-1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1), 
                morral(tamano_morral, pesos, valores,  n-1))

def main():
    valores = [100, 200, 300]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print (resultado)

if __name__ == "__main__":
    main()