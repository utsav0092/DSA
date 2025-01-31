'''Rotate array by one position'''
'''TC = O(n) and SC = O(1)'''

# def RotateByOne(arr):
#     n = len(arr)
#     temp = arr[0]
#     for i in range(1, n):
#         arr[i-1] = arr[i]
#     arr[n-1] = temp
#     return arr

# arr = [1, 2, 3, 4, 5]
# print(RotateByOne(arr))

'''Leetcode - Rotate an array by k position'''

def RotateByK(arr, k):
    j = 1
    n = len(arr)
    for i in range(k):
        temp = arr[0]
        while (j < n):
            arr[j-1] = arr[j]
            j += 1
        arr[n-1] = temp
    return arr

    # [3, 4, 5, 1, 2]
arr = [1, 2, 3, 4, 5]
k = 2
print(RotateByK(arr, k))