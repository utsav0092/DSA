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

'''Optimised solution (Moose's voring algorithm)'''
'''tc - O() and sc - O()'''

def major(arr):
    return arr

def main():
    arr = [1,2,2,2,2]
    print(major(arr))

if __name__ == "__main__":
    main()