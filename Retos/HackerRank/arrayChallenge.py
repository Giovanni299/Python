# For each element of an array, a counter is set to 0. The element is compared to each element to its left. If
# the element to the left is greater, the absolute difference is subtracted from the counter. If the element to
# the left is less, the absolute difference is added to the counter. For each element of the array, determine
# the value of the counter. These values should be stored in an array and returned.


def arrayChallenge(arr):
    n = len(arr)
    ans = [0] * n
    sum = arr[0] # prefix sum
    for i in range(1, n):
        ans[i] = arr[i] * i - sum
        sum += arr[i]

    return ans

# print(arrayChallenge([2,4,3])) #[0, 2, 0]
# print(arrayChallenge([2,1,3])) #[0,-1,3]
print(arrayChallenge([1,2,2,3])) #[0,1,1,4]