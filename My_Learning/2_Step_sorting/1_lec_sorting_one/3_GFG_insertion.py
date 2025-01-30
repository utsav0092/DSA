'''GFG solution for Insertion sort using python'''

def insertion(arr):
    n = len(arr)
    for i in range(1, n): # 1 to n-1
        j = i
        while (j > 0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(f"Before sorting: {arr}")
    print(f"After sorting: {insertion(arr)}")