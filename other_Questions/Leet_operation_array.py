'''Leetcode - Perform nth operation on array'''
'''My solution'''

def Array(nums):
    n = len(nums)
    i = 0
    j = 1
    while (j < n):
        if (nums[i] == nums[j]):
            nums[i] = nums[i]*2
            nums[j] = 0
        i += 1
        j += 1
    nums = moveZero(nums)
    return nums

def moveZero(nums):
    n = len(nums)
    i = 0
    j = -1
    for i in range(n):
        if (nums[i] == 0):
            j = i   
            break
    for i in range(j+1, n):
        if (nums[i] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

#      [1,4,0,6,0,4,5]
nums = [1,2,2,3,3,4,5]
print(Array(nums))