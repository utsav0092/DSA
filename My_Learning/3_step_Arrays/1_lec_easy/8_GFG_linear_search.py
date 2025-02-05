'''GFG - Find the element using linear search'''
'''Time Complexity: O(n) and Space Complexity: O(1)'''

def linearSearch(nums, key):
    n = len(nums)
    for i in range(n):
        if nums[i] == key:
            return True
    return False

nums = [1, 2, 3, 4, 5]
key = 4
print(linearSearch(nums, key))