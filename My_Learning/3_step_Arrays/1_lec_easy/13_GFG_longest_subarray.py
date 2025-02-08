'''GFG - Longest subarray with sum K'''
'''TC - O(n^3) and SC - O(n)'''

# def longSubArray(nums, k):
#     n = len(nums)
#     length = 0
#     for i in range(n):
#         for j in range(i, n):
#             s = 0
#             for m in range(i, j + 1):
#                 s = s + nums[m]
#             if s == k:
#                 length = max(length, j - i + 1)
#     return length 

# def main():
#     nums = [1,1,1,1,1,2,3,4,5]
#     k = 5
#     print(longSubArray(nums, k))

# if __name__ == "__main__":
#     main()

#-----------------------------------------------------------------------------

'''Another approach'''
'''TC - O(n^2) SC - O(n)'''

# def subArray(nums, k):
#     n = len(nums)
#     length = 0
#     for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s = s + nums[j]
#         if s == k:
#             length = max(length, j-i+1)
#     return length

# def main():
#     nums = [1,1,1,1,1,2,3,4,5]
#     k = 5
#     print(subArray(nums, k))

# if __name__ == "__main__":
#     main()

#---------------------------------------------------------------------------------------------

'''Better approach'''

