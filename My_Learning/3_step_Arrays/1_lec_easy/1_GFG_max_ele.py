'''Find the max element in the array'''
'''With sorting'''

# def findMax(arr):
#     arr.sort()
#     return arr[-1]

# arr = list(map(int, input().split()))
# print(f"Max Element is: {findMax(arr)}")

'''Without using sort'''

'''Optimised TC = O(n) and SC = O(n)'''

def findMax(arr):
    m = arr[0]
    for i in range(len(arr)):
        if (arr[i] > m):
            arr[i], m = m, arr[i]
    return m

arr = list(map(int, input().split()))
print(f"Max Element is: {findMax(arr)}")