'''Leetcode - Move zero to end'''
'''TC - O(2n) and SC - O(n) (worst)'''

# def moveZero(nums):
#     n = len(nums)
#     temp = []
#     for i in range(n):
#         if (nums[i] != 0):
#             temp.append(nums[i])
#     tempn = len(temp)
#     for i in range(tempn):
#         nums[i] = temp[i]
#     for i in range(tempn, n):
#         nums[i] = 0
#     return nums

# nums = [1,2,0,3,0,4,0]
# print(moveZero(nums))

'''Optimised solution (2-pointer)'''
'''Tc - O(n) and SC - O(1)'''

def moveZero(nums):
    n = len(nums)
    j = -1
    for i in range(n):
        if (nums[i] == 0):
            j = i
            break
    if (j == -1):
        return nums
    for i in range(j+1, n):
        if (nums[i] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            j =+1
    return nums

nums = [1,2,0,3,4,0,5,6,0]
print(moveZero(nums))