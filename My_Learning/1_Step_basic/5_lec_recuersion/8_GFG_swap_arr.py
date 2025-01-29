'''Reverse an array using recursion with two pointers'''
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

'''Reverse an array using loop with one pointer'''
class Reverse:
    def reverse_array(self, arr, n):
        i = 0
        for i in range(len(arr)):
            if (i >= n//2):
                return arr
            else:
                arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

if __name__ == "__main__":
    r = Reverse()
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print(r.reverse_array(arr, n))

'''Reverse an array using recursion with one pointer'''
class Recursion:
    def reverse_array(self, arr, i=0):
        n = len(arr)
        if (i >= n // 2): 
            return arr
        else:
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
            return self.reverse_array(arr, i + 1)

if __name__ == "__main__":
    r = Recursion()
    arr = [1, 2, 3, 4, 5]
    print(r.reverse_array(arr))