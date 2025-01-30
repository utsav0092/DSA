'''GFG my code for bubble sort'''
'''Time Complexity is O(n^2)'''

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] >= arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    arr = [2,1,2,3,4,5,6,3,4,5,6,7,8,9,2,10,1]
    print(f"Before sorting: {arr}")
    print(f"After sorting: {bubbleSort(arr)}")  

'''Striver approach'''
'''Time Complexity O(n)'''

def bubbleSort(arr):
    for i in range(len(arr) - 1):  # Outer loop for passes
        didswap = False  # Track if any swaps occurred in this pass
        for j in range(len(arr) - 1 - i):  # Inner loop for comparisons
            print(f"Pass {i + 1}, comparing indices {j} and {j + 1}")
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if necessary
                didswap = True
        if not didswap:  # If no swaps occurred, the array is already sorted
            break

    return arr

if __name__ == "__main__":
    arr = [3, 2, 1, 4, 5, 6]
    print(f"Before sorting: {arr}")
    print(f"After sorting: {bubbleSort(arr)}")