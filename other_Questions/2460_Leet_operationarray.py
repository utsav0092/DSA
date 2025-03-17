'''Leetcode - Perform the operations on the given array'''
'''My approach'''

# def oparray(nums):
#         n = len(nums)
#         i = 0
#         j = 1
#         while (j < n):
#             if (nums[i] == nums[j]):
#                 nums[i] = nums[i]*2
#                 nums[j] = 0
#             i += 1
#             j += 1
#         nums = moveZero(nums)
#         return nums

# def moveZero(nums):
#     print(nums)
#     n = len(nums)
#     i = 0
#     j = 0
#     for i in range(n):
#         if (nums[i] == 0):
#             j = i   
#             break
#     for i in range(j+1, n):
#         if (nums[i] != 0):
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#     return nums

# def main():
#      arr = [1, 1, 2, 2, 3, 3]
#      print(oparray(arr))

# if __name__ == "__main__":
#      main()

'''----------------------------------------------------------------------------------------------------------------'''
'''corrected one'''

def oparray(nums):
      n = len(nums)
      # Step 1: Apply the operations
      for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
      # Step 2: Move zeroes to the end using two-pointer method
    #   nums = moveZeroes(nums)
      moveZeroes(nums)
      return nums

def moveZeroes(nums):
    n = len(nums)
    pos = 0  # Position to place the next non-zero element
    for i in range(n):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    # return nums

def main():
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    print(oparray(nums))

if  __name__ == "__main__":
    main()