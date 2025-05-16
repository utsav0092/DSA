'''Leetcoe - Next permutation'''
'''tc :- O(3n) and sc :- O(1)'''
'''optimal force'''

def permutation(arr):
    n = len(arr)
    index = -1

    '''Step 1: Find the longest prefix match'''
    for i in range(n-2, -1, -1):  # Fix: Loop should go down to -1
        if arr[i] < arr[i+1]:
            index = i
            break  # Fix: Stop at the first occurrence

    '''Edge Case: If the array is in descending order, return the smallest permutation'''
    if index == -1:
        arr.reverse()  # Fix: Reverse in-place, then return arr
        return arr

    '''Step 2: Find the smallest element larger than arr[index] from the right'''
    for i in range(n-1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]  # Swap elements
            break

    '''Step 3: Reverse the part after index to get the next permutation'''
    arr[index + 1:] = reversed(arr[index + 1:])  # Reverse suffix

    return arr  # Fix: Return the modified list

arr = [1, 3, 2]
print(permutation(arr))  
