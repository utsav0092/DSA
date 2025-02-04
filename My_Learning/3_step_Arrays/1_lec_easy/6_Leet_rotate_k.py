'''Leetcode - Rotate an array by k position'''
'''Optimised Solution'''

# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n  # Handle cases where k > n
#         # Reverse the entire array
#         nums.reverse() # [7, 6, 5, 4, 3, 2, 1] 
#         # Reverse the first k elements
#         nums[:k] = reversed(nums[:k]) # return reversed part [5, 6, 7, 4, 3, 2, 1]
#         # Reverse the remaining elements
#         nums[k:] = reversed(nums[k:]) # [5, 6, 7, 1, 2, 3, 4]

# nums = list(map(int, input("Enter the list values: ").split()))
# k = int(input("Enter the value: "))
# sol = Solution()
# sol.rotate(nums, k)
# print(nums) 

'''Striver Brute force solution'''
'''TC - O(n+d) SC = O(d)'''

# def Rotate(nums, k):
#     n = len(nums)
#     k = k % n
#     temp = []
#     for i in range(k):
#         temp.append(nums[i])
#     for i in range(k, n):
#         nums[i-k] = nums[i]
#     for i in range(n-k, n):
#         nums[i] = temp[i-(n-k)]
#     return nums        

# nums = [1,2,3,4,5,6,7]
# k = 3
# Rotate(nums, k)
# print(nums)