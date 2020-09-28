
def braces(values):
    result = []
    for value in values:
        if len(value) % 2 != 0:
            result.append('NO')
            continue
        
        result.append(matchingBraces(value))        

    return result

def matchingBraces(value):
    closed = {')':'(', '}':'{', ']':'['}
    stack = [] 
    temp = ''
    for val in value:
        if val not in closed:
            stack.append(val)
            temp = val
        elif val in closed:
            open = closed.get(val)
            if open != temp:
                return 'NO'
                
            stack.pop()
            if len(stack) == 0:
                temp = ''  
            else:
                temp = stack.pop()
                stack.append(temp)
    
    return 'YES' if len(stack) == 0 else 'NO'


if __name__ == '__main__':
    #val = ['{[}]}}']
    val = ['{[()]}']
    print(braces(val))