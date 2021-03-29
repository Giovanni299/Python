import string

def rollingString(s, operations):
    alpha = string.ascii_lowercase
    len_alpha = len(alpha)
    result = list(s)
    for oper in operations:
        oper = oper.split()
        for j in range(int(oper[0]), int(oper[1])+1):
            pos = (alpha.index(result[j]) - 1) % len_alpha if oper[2] == 'L' else (alpha.index(result[j]) + 1) % len_alpha
            result[j] = alpha[pos]
    
    return ''.join(result)

print(rollingString('abc', ["0 0 L", "2 2 L", "0 2 R"])) #acc
print(rollingString('abc', ["0 1 L", "1 2 R", "0 2 R"])) #ace