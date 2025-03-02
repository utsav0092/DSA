'''Leet - Remove duplicates from the sorted in-array'''
'''using set directly'''

# def Rdup(arr):
#     arr = set(arr)
#     return list(arr)

# arr = list(map(int, input().split()))
# print(Rdup(arr))

'''Using two pointer to get optimal solution'''
'''TC = O(n) and SC = O(1)'''

# def Rdup(arr):
#     n = len(arr)
#     i = 0
#     j = 1
#     #[1, 1, 2, 2, 3, 3, 4, 5]
#     while (j < n):
#         if (arr[i] == arr[j]):
#             j += 1
#         else:
#             i += 1
#             arr[i] = arr[j]
#     return arr[:i]
#     # return i

# arr = [1, 1, 2, 2, 3, 3, 4, 5]
# print(Rdup(arr))

'''other solution'''

# from typing import List
# def removeDuplicates(nums: List[int]) -> int:
#     l = 1
#     for r in range(1, len(nums)):
#         if nums[r] != nums[r-1]:
#             nums[l] = nums[r]
#             l += 1
#     for i in range(l, len(nums)):
#         nums.pop()
#     return nums

# def main():
#     nums = [1,1,3,3,4,5]
#     print(removeDuplicates(nums))

# if __name__ == "__main__":
#     main()