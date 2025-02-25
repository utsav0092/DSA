'''Leetcode - 2 sum problem'''
'''My Brute force : tc - O(n^2) and sc - O(1)'''

def twoSum(arr, k):
    n = len(arr)
    i = 0
    j = 0
    while (i < n):
        while (j < n):
            if arr[i] + arr[j] == k:
                return arr[i], arr[j]
            else:
                j += 1
        i += 1

def main():
    arr = [3,3,2,2,1]
    k = 6
    print(twoSum(arr, k))

if __name__ == "__main__":
    main()

'''Striver's code Brute force'''
'''tc - O(n^2) and sc - O(1)'''

def twoSum(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i] + arr[j] == k:
                return arr[i], arr[j]

def main():
    arr = [3,3,2,2,1]
    k = 6
    print(twoSum(arr, k))

if __name__ == "__main__":
    main()

'''Better solution (with map)'''
'''tc - O(n) and sc - O(n)'''

def twoSum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return -1
    
def main():
    nums = [1,2,3,4,5]
    target = 9
    print(twoSum(nums, target))

if __name__ == "__main__":
    main()

'''Optimal appraoch (two pointer)'''
'''tc - O(n) / O(nlogn) for sorting and sc - O(1)'''

def twoSum(target, nums):
    n = len(nums)
    i = 0
    j = n-1
    nums.sort()
    while (i < j):
        if nums[i] + nums[j] == target:
            # return [i, j]
            return [nums[i], nums[j]]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return -1
def main():
    nums = [1,2,3,4,5]
    target = 9
    print(twoSum(target, nums))

if __name__ == "__main__":
    main()