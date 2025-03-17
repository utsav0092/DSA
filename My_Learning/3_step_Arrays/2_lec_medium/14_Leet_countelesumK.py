'''Leetcode - Count the number of subarrays whose sum equals K '''
'''TC: O(n^2), SC: O(1)'''  
'''Better solution'''

# def sumEqual(arr, k):
#     n = len(arr)
#     count = 0

#     for i in range(n):
#         summ = 0  
#         for j in range(i, n):
#             summ += arr[j]
#             if summ == k:
#                 count += 1
#                 print("Valid subarray:", arr[i:j+1]) 

#     return count

# def main():
#     arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]  # Expected total subarrays: 8
#     k = 3
#     print("Total subarrays:", sumEqual(arr, k))

# if __name__ == "__main__":
#     main()

'''--------------------------------------------------------------------------------------------------'''

'''Optimised solution (prefix-sum / hashmap)'''
'''tc - O(n) and sc - O(n)'''

# def sumEqual(arr, k):

#     n = len(arr)
#     hash_map = {0:1}
#     prefixsum = 0
#     total = 0

#     for i in range(n):
#         prefixsum += arr[i]
#         remove = prefixsum - k
#         if remove in hash_map:
#             total += hash_map[remove]
#             print('total: ',total)
#         if prefixsum in hash_map:
#             hash_map[prefixsum] += 1
#             print('1_hash_map[prefixsum]:- ',hash_map[prefixsum])
#             print()
#         else:
#             hash_map[prefixsum] = 1
#             print('2_hash_map[prefixsum]:- ',hash_map[prefixsum])
#             print()

#     return total

# def main():
#     arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]  # Expected total subarrays: 8
#     k = 3
#     print("Total subarrays:-", sumEqual(arr, k))

# if __name__ == "__main__":
#     main()