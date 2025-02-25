'''Leetcoee - Sort the 0's, 1's and 2's'''
'''with sort() tc - O(nlogn) and sc - O(n)'''

# def arrange(nums):
#     nums.sort()
#     return nums

# def main():
#     nums = [0,1,2,0,1,2,0,1,2]
#     print(arrange(nums))

# if __name__ == "__main__":
#     main()

'''Striver's solution'''
'''tc - O(2n) and sc - O(1)'''

# def arrange(nums):
#     n = len(nums)
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     for i in nums:
#         if i == 0:
#             count0 += 1
#         elif i == 1:
#             count1 += 1
#         elif i == 2:
#             count2 += 1
#     for i in range(count0):
#         nums[i] = 0
#     for i in range(count0, n):
#         nums[i] = 1
#     for i in range((count0 + count1), n):
#         nums[i] = 2
#     return nums

# def main():
#     nums = [1,0,2,1,0,1,2,0,1]
#     print(arrange(nums))

# if __name__ == "__main__":
#     main() 

'''Optimised solution (Dutch National Flag Algo (3-pointers))'''
'''
[0 ...... low-1] -> 0 extreme left
[low ...... mid-1] -> 1
[mid ...... high] -> random value
[high+1 ...... n-1] -> 2 extreme right
'''
'''tc - O(n) and sc - O(1)'''

# def arrange(nums):
#     n = len(nums)
#     low = 0
#     mid = 0
#     high = n-1
#     while (mid <= high):
#         if (nums[mid] == 0):
#             nums[low], nums[mid] = nums[mid], nums[low]
#             mid += 1
#             low += 1
#         elif (nums[mid] == 1):
#             mid += 1
#         elif (nums[mid] == 2):
#             nums[high], nums[mid] = nums[mid], nums[high]
#             high -= 1
#     return nums
# def main():
#     nums = [0,0,2,2,1,1,2,0,2,1,0,0]
#     print(arrange(nums))

# if __name__ == "__main__":
#     main()  