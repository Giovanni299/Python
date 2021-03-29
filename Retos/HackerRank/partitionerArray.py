import collections

def partitionArray(k, numbers):
    # Write your code here
    len_num = len(numbers)
    
    if k > len_num or len_num%k:
        return 'No' 
    
    counter = collections.Counter(numbers)
    # print(counter)
    if len_num // k < max(counter.values()):
        return 'No'
    
    return 'Yes'

print(partitionArray(4,[8,3,6,5,7]))