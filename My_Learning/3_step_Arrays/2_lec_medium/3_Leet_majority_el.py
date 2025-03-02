'''Leetcode - Majority element appear ()> n/2 times)'''
'''Brute force tc - O(n^2) and sc - O(1)'''

# def major(arr):
#     n = len(arr)
#     check = n // 2
#     for i in range(n):
#         count = 0
#         for j in range(n):
#             if arr[i] == arr[j]:
#                 count += 1
#         if count > check:
#             return arr[i]
#     return -1

# def main():
#     arr = [1,2,2,2,2]
#     print(major(arr))

# if __name__ == "__main__":
#     main()

'''Better solution (hashmap)'''
'''tc - O(2n) and sc - O(n)'''

# def major(arr):
#     n = len(arr)
#     match = n // 2
#     hash_map = {}
#     for num in arr:
#         if num not in hash_map:
#             hash_map[num] = 1
#         else:
#             hash_map[num] += 1
#     for  key, val in  hash_map.items():
#         if val > match:
#             return key
#     return -1

# def main():
#     arr = [1,2,2,2,2]
#     print(major(arr))

# if __name__ == "__main__":
#     main()

'''Better solution (using Counter)'''
'''tc - O(n) and sc - O(n)'''

# from collections import Counter

# def major(arr):
#     n = len(arr)
#     count = Counter(arr)
#     for key, val in count.items():
#         if val > n//2:
#             return key
#     return -1

# arr = [1,1,1,1,2,3]
# print(major(arr))

'''Optimised solution (Moore's voting algorithm)'''
'''tc - O(n) and sc - O(1)'''

# def major(arr):
#     n = len(arr)
#     count = 0
#     c = 0

#     for i in range(n):
#         if count == 0:
#             count = 1
#             el = arr[i]
#         elif arr[i] == el:
#             count += 1
#         else:
#             count -= 1

#     for j in range(n):
#         if arr[j] == el:
#             c += 1

#     if c > n//2:
#         return el
#     else:
#         return -1

# def main():
#     arr = [1,3,3,3,3,3,3,3,4,5,4,3]
#     print(major(arr))

# if __name__ == "__main__":
#     main()