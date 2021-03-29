#Matrix Script
#https://www.hackerrank.com/challenges/matrix-script/problem

import math
import os
import random
import re
import sys
import numpy as np 
import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text = ''.join(matrix[j][i] for i in range(m) for j in range(n))

print(text)
#print(re.sub(r"(?<=\w)([^\w])([^\w])"," ", text))
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)"," ", text))
##print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', " ", text))

'''
Input:
========================
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

========================
3 3
123
456
789
'''
