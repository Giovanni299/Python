def divide_List(data_list, divisor):
    try:
        return [i / divisor for i in data_list]
    except ZeroDivisionError as e:
        print(f'****EXCEPTION: {e}')
        return data_list

data_list = list(range(0,11,2))
divisor = 0

print(data_list)
print(divide_List(data_list, divisor))