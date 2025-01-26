'''GFG solution of Selection sort'''

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1): #start 0 to n-2
        min_index = i # setting the first index as min
        for j in range(i + 1, n): #start i+1 to n-1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11]
    print(f"Before sorting: {arr}")
    print(f"After sorting: {selectionSort(arr)}")