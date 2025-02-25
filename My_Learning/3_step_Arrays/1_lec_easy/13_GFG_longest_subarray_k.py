'''GFG - Longest subarray with sum k'''
'''Brute force solution tc - O(n^3) and sc - O(1)'''
'''Brute force solution of the best case tc - O(n^2) and sc - O(1)'''

# def subArray(arr, k):
#     n = len(arr)
#     length = 0
#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             # summ = 0
#             # for m in range(i, j+1):
#                 # summ = summ + arr[m]
#                 summ = summ + arr[j]
#                 if summ == k:
#                     length = max(length, j-i+1)
#     return length

# def main():
#     arr = [1,2,3,4,5]
#     k = 5
#     print(subArray(arr, k))

# if __name__ == "__main__":
#     main()

#---------------------------------------------------

'''Better apraoch for (Both) using (hashmap and Prefixsum algorithm)'''
'''tc - O(n) and sc - O(n)'''

# def subArray(arr, k):
#     pre_sum_map = {0: -1}  # Stores prefix sum and its first occurrence index
#     summ = 0
#     maxlen = 0
    
#     for i in range(len(arr)):
#         summ += arr[i]  # Calculate prefix sum
#         if summ == k:
#             maxlen = max(maxlen, i + 1)  # If sum matches k, update maxlen
#         rem = summ - k  # Find the required remaining sum
#         if rem in pre_sum_map:
#             lenn = i - pre_sum_map[rem]  # Calculate subarray length
#             maxlen = max(maxlen, lenn)  # Update maxlen
#         if summ not in pre_sum_map:  # Store first occurrence only
#             pre_sum_map[summ] = i
#     return maxlen

# def main():
#     arr = [10, 5, 2, 7, 1, -10]
#     k = 15
#     print(f"The largest subarray values is: {subArray(arr, k)}") 

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------------------

'''Optimised apraoch for (positives and zeros) using (two pointers and greedyalgorithm)'''
'''tc - O(2n) and sc - O(1)'''

# def subArray(arr, k):
#     n = len(arr)
#     summ = 0
#     maxlen = 0
#     right = 0
#     left = 0
#     while (right < n):
#         while (left <= right and summ > k):
#             summ -= arr[left]
#             left += 1
#         if (summ == k):
#             maxlen = max(maxlen, right - left + 1)
#         right += 1
#         if (right < n):
#             summ += arr[right]
#     return maxlen

# def main():
#     arr = [10, 5, 2, 7, 1, 10]
#     k = 15
#     print(f"The largest subarray values is: {subArray(arr, k)}") 

# if __name__ == "__main__":
#     main()