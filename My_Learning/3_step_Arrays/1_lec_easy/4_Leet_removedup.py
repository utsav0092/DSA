'''Leet - Remove duplicates from the sorted in-array'''
'''using set directly'''

def Rdup(arr):
    arr = set(arr)
    return list(arr)

arr = list(map(int, input().split()))
print(Rdup(arr))

'''Using two pointer to get optimal solution'''
'''TC = O(n) and SC = O(1)'''

def Rdup(arr):
    n = len(arr)
    i = 0
    j = 1
    #[1, 1, 2, 2, 3, 3, 4, 5]
    while (j < n):
        if (arr[i] == arr[j]):
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
    return arr[:i]
    # return i

arr = [1, 1, 2, 2, 3, 3, 4, 5]
print(Rdup(arr))