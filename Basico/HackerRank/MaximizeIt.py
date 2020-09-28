#https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product

k,m = [int(i) for i in input().split()]
list_n = []
for n in range(k):
    list_n.append([int(i) for i in input().split()][1:])

#print(list_n)

results = map(lambda x: sum(i**2 for i in x) % m, product(*list_n))
print(max(results))

'''
Copiar y pegar los valores
3 100
3 2 5 4
4 3 7 8 9
6 5 5 7 8 9 10


7 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
2 5 4
3 7 8 9
5 5 7 8 9 10
1 10


3 3
1 2 3
2 4 6
3 6 9


3 100
5 2 5 4
9 3 7 8 9
10 5 5 7 8 9 10
'''