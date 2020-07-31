import random

def getCoupon(amount, valores, n):
    pos = ""

    if n == 0 or amount == 0:
        return 0, pos

    if valores[n-1] > amount:
        return getCoupon(amount, valores, n-1)

    val1, pos1 = getCoupon(amount - valores[n - 1], valores, n - 1)
    val2, pos2 = getCoupon(amount, valores, n-1)
    if valores[n-1] + val1 >= val2:
        final = valores[n-1] + val1
        pos = pos1 +","+ str(n)
    else:
        final = val2 
        pos = pos2  

    #print(f'pos1: {val1}, pos2: {val2}, final: {final}, pos: {pos}')
    return final, pos

def main():
    valores = [random.randint(0, 400) for i in range(7)]#[80, 201, 175, 90, 10, 280, 270]
    print (valores)

    amount = 500
    n = len(valores)
    resultado, pos = getCoupon(amount, valores, n)
    print (resultado)
    print (pos)

if __name__ == "__main__":
    main()
