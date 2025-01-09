class Recursion:
    def swapArray(self, arr, l, r):
        if l >= r:
            return arr
        else:
            # Swap the elements
            arr[l], arr[r] = arr[r], arr[l]
            # Recursively call swapArray with updated indices
            return self.swapArray(arr, l + 1, r - 1)

if __name__ == '__main__':
    r = Recursion()
    arr = [1, 2, 3, 4, 5]
    # Call swapArray with initial indices l=0 and r=len(arr)-1
    result = r.swapArray(arr, 0, len(arr) - 1)
    print(result)  # Output: [5, 4, 3, 2, 1]