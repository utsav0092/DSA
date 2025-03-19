'''Leetcode - find the kth distance elements form the given key value'''
'''brute force'''
'''tc - O(n^2) and sc - O(n)'''

# def findKDistantIndices(nums, key, k):
#     n = len(nums)
#     key_positions = [j for j in range(n) if nums[j] == key]  # Step 1: Find key positions
#     result = set()  # Using a set to avoid duplicates

#     for i in range(n):  # Step 2: Check each index i
#         for j in key_positions:
#             if abs(i - j) <= k:  # Step 3: Check distance condition
#                 result.add(i)
#                 break  # No need to check further for this i

#     return sorted(result)  # Step 4: Return sorted list

# # Example Usage
# nums = [3,4,9,1,3,9,5]
# key = 9
# k = 1
# print(findKDistantIndices(nums, key, k))  # Output: [1,2,3,4,5,6]

'''Optimised solution (two pointers)'''
'''tc - O(n) and sc - O(n)'''

# def findKDistantIndices(nums, key, k):
#     n = len(nums)
#     key_positions = [i for i in range(n) if nums[i] == key]  # Step 1: Find all indices of 'key'
#     result = []
#     j = 0  # Pointer for key_positions

#     for i in range(n):  # Step 2: Iterate through the array
#         # Move 'j' to keep it within the valid range
#         while j < len(key_positions) and key_positions[j] < i - k:
#             j += 1  
        
#         # If the current key_positions[j] is within k distance, add i to the result
#         if j < len(key_positions) and abs(i - key_positions[j]) <= k:
#             result.append(i)

#     return result  # Step 3: Return result list

# # Example Usage
# nums = [3,4,9,1,3,9,5]
# key = 9
# k = 1
# print(findKDistantIndices(nums, key, k))  # Output: [1,2,3,4,5,6]