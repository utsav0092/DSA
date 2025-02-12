'''Leetcode - 2 sum problem'''
'''My Brute force : tc - O(n^2) and sc - O(1)'''

# def twoSum(arr, k):
#     n = len(arr)
#     i = 0
#     j = 0
#     while (i < n):
#         while (j < n):
#             if arr[i] + arr[j] == k:
#                 return arr[i], arr[j]
#             else:
#                 j += 1
#         i += 1

# def main():
#     arr = [3,3,2,2,1]
#     k = 6
#     print(twoSum(arr, k))

# if __name__ == "__main__":
#     main()

'''Striver's code Brute force'''
'''tc - O(n^2) and sc - O(1)'''

# def twoSum(arr, k):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue
#             if arr[i] + arr[j] == k:
#                 return arr[i], arr[j]

# def main():
#     arr = [3,3,2,2,1]
#     k = 6
#     print(twoSum(arr, k))

# if __name__ == "__main__":
#     main()

'''Better solution (hasing)'''

def twoSum(arr, k):
    n = len(arr)
    
def main():
    arr = [3,3,2,2,1]
    k = 6
    print(twoSum(arr, k))

if __name__ == "__main__":
    main()