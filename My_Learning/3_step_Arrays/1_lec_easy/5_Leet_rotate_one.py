'''Rotate array by one position'''
'''TC = O(n) and SC = O(1)'''

def RotateByOne(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1, 2, 3, 4, 5]
print(RotateByOne(arr))