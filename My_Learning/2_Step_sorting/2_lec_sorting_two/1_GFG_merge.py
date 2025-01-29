'''GFG solution for Merge sort using python'''

def MergeSort(arr, low, high):
    if (low == high):
        return
    else:
        mid = (low + high) // 2
        MergeSort(arr, low, mid)
        MergeSort(arr, mid + 1, high)
        Merge(arr, low, mid, high)

# Merge function to merge two sorted subarrays
def Merge(arr, low, mid, high):
    # [low...mid] and [mid+1...high]
    temp = []
    left = low
    right = mid + 1

    # Compare elements from both subarrays and add the smaller one to temp
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])  # Fixed: Correctly append the smaller element from the left subarray
            left += 1
        else:
            temp.append(arr[right])  # Fixed: Changed from temp.right to temp.append to fix method error
            right += 1

    # Add any remaining elements from the left subarray
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # Add any remaining elements from the right subarray
    while (right <= high):  # Fixed: Corrected condition from "right <= arr[right]" to "right <= high"
        temp.append(arr[right])
        right += 1

    # Copy the sorted elements back into the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    low = 0
    high = len(arr) - 1
    print(f"Before sorting: {arr}")
    MergeSort(arr, low, high)  # Note: MergeSort modifies the array in place
    print(f"After sorting: {arr}") 