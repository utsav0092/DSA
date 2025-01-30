'''Leetcode - Check if the array is sorted or nont'''
'''TC = O(n) and SC = O(n) (my approch)'''

def if_Sorted(arr):
    i = 0
    j = i + 1
    while (j < len(arr)):
        if (arr[i] < arr[j]):
            i += 1
            j += 1
        else:
            return False
    return True

arr = list(map(int, input("Enter values: ").split()))
print(if_Sorted(arr))

'''Stiver code'''

def if_Sorted(arr):
    for i in range(1, len(arr)):
        if (arr[i-1] < arr[i]):
            pass
        else:
            return False
    return True

arr = list(map(int, input("Enter values: ").split()))
print(if_Sorted(arr))