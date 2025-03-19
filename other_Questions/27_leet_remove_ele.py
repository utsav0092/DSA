'''Leetcode -  Remove given element from the array nums'''
'''tc - O(n) and sc - O(1)'''

def removeEle(nums, val):
    # newArray = []
    # for i in nums:
    #     if i != val:
    #         newArray.append(i)
    # return newArray

    # n = len(nums)
    # i = 0
    # j = i + 1
    # k = 0
    # while (j < n):
    #     if nums[j] != val:
    #         nums[j], nums[i] = nums[i], nums[j]
    #         k += 1
    #         i += 1
    #         j += 1
    #     else:
    #         j += 1
    # return nums[:k]

    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

nums = [3, 2, 2, 3]
val = 3
k = removeEle(nums, val)
print(nums[:k])