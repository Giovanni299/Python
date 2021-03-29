# Los sistemas multiprocesador utilizan varias CPU para realizar diversas tareas. Esto aumenta el rendimiento y reduce el tiempo de 
# respuesta. En este problema, un sistema multiprocesador tiene un cierto número de procesadores. Cada procesador tiene la capacidad 
# de programar un número limitado de procesos en un segundo. Sin embargo, después de este la capacidad del procesador se reduce 
# al piso (capacidad / 2). Dadas las capacidades del procesador y el número de procesos, ¿cuál es el tiempo mínimo requerido para
# programar todos los procesos en el sistema?


# https://docs.python.org/es/3/library/heapq.html
# https://rico-schmidt.name/pymotw-3/heapq/index.html

import heapq as hq
import math
from io import StringIO

def show_tree(tree, total_width=36, fill=' '):
    """Pretty-print a tree."""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2 ** row
        col_width = int(math.floor(total_width / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print('-' * total_width)

def minimumTime(ability, processes):
    max_values = [-x for x in ability]
    hq.heapify(max_values)
    # show_tree(max_values)
    count = 0
    while (processes > 0):
        value = -hq.heappop(max_values)
        processes -= value
        count += 1

        hq.heappush(max_values, -(value//2))
        # show_tree(max_values)

    return count 


ability = [3, 1, 7, 2, 4] 
processes = 15 
print(minimumTime(ability, processes))

ability =[2, 1, 5, 3, 1]
processes = 17 
print(minimumTime(ability, processes))
