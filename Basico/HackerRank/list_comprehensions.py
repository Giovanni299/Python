#https://www.hackerrank.com/challenges/list-comprehensions/problem
from itertools import product

def comprehensions(x,y,z,n):
    w=[list(range(x+1)), list(range(y+1)), list(range(z+1))]
    q = filter(lambda x: sum(x) != n , product(*w))  
    return [list(i) for i in q]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(comprehensions(x,y,z,n))
