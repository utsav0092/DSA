'''GFG solution for quick sort using python'''

def quickSort(arr, low, high):
    if low < high:
        part = find(arr, low, high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)
    return arr

def find(arr, low, high):
    pivot = arr[low]
    i = low + 1 
    j = high

    while i <= j:
        while i <= high and arr[i] <= pivot:  # Ensure i does not exceed high
            i += 1
        while j >= low and arr[j] > pivot:  # Ensure j does not go below low
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[low], arr[j] = arr[j], arr[low]  # Place pivot at correct position
    return j  # Return the correct pivot position

# Driver Code
if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers: ").split()))
    low = 0
    high = len(arr) - 1
    print("Sorted array:", quickSort(arr, low, high))