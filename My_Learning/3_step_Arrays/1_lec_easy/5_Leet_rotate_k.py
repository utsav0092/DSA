'''Rotate array by one position'''
'''TC = O(n) and SC = O(1)'''

def RotateByOne(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp
    return arr

arr = [1, 2, 3, 4, 5]
print(RotateByOne(arr))

'''Leetcode - Rotate an array by k position'''

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle cases where k > n
        # Reverse the entire array
        nums.reverse() # [7, 6, 5, 4, 3, 2, 1] 
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k]) # return reversed part [5, 6, 7, 4, 3, 2, 1]
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:]) # [5, 6, 7, 1, 2, 3, 4]

nums = list(map(int, input("Enter the list values: ").split()))
k = int(input("Enter the value: "))
sol = Solution()
sol.rotate(nums, k)
print(nums) 