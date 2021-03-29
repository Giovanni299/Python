# Maximizing the Final Element 
# Given an array of integers, perform certain operations in order to satisfy some constraints. The constraints
# are as follows:
# The first array element must be 1.
# For all other elements, the difference between adjacent integers must not be greater than 1. In other
# words, for 1 ≤ i < n, arr[i] - arr[i-1] ≤ 1.
# To accomplish this, the following operations are available:
# Rearrange the elements in any way.
# Reduce any element to any number that is at least 1.
# What is the maximum value that can be achieved for the final element of the array by following these
# operations and constraints?


def getMaximunValue(arr):
    arr.sort()
    n = len(arr)
    value = 1
    for i in range(1, n):
        if (arr[i] - value > 1):
            value += 1
        else:
            value = arr[i]
    
    return value


print(getMaximunValue([3, 1, 3, 4])) #4
print(getMaximunValue([1, 3, 2, 2])) #3
print(getMaximunValue([3, 2, 3, 5])) #4