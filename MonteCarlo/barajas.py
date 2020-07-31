import random
import collections

PALOS = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
VALORES = ['AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Queen', 'King']

def crearBarajas():
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo, valor))

    return baraja

def obtener_mano(baraja, num_mano):
    return random.sample(baraja, num_mano)

def main(tamano_mano, intentos):
    baraja = crearBarajas()
    manos = []

    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)
    
    pares = 0
    trios = 0
    for mano in manos:
        valores = []
        hay_par = True
        for carta in mano:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 3:
                trios += 1
                if hay_par:
                    pares += 1
                break
            
            if hay_par and val == 2:
                pares += 1
                hay_par = False
        
    probabilidad_par = pares / intentos
    probabilidad_trio = trios / intentos
    print(f'La probabilidad de obtener un PAR en una mano de {tamano_mano} cartas es {probabilidad_par}')
    print(f'La probabilidad de obtener un TRIO en una mano de {tamano_mano} cartas es {probabilidad_trio}')

if __name__ == "__main__":
    tamano_mano = int(input('Numero de cartas: '))
    intentos = int(input('Numero de intentos: '))
    main(tamano_mano, intentos)