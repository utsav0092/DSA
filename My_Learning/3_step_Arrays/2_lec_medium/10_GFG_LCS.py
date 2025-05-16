'''Leetcode - Longest Common Subsequence'''
'''Brute solution'''
'''tc - O(n^2) and sc - O(n)'''

# def LCSnum(arr):
#     num_set = set(arr)
#     longest = 0

#     for num in num_set:
#         if num - 1 not in num_set:
#             current_num = num
#             count = 1

#             while current_num + 1 in num_set:
#                 current_num += 1
#                 count += 1

#             longest = max(longest, count)

#     return longest

# def main():
#     arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
#     print(LCSnum(arr))  

# if __name__ == "__main__":
#     main()

'''-----------------------------------------------------------------------------------------------------'''

'''Better solution'''
'''tc - O(nlogn) and sc - O(1)'''

# def LCSnum(arr):
#     n = len(arr)

#     arr = sorted(arr)
#     longest = 1
#     count_current = 0
#     last_smallest = float('-inf')

#     for i in range(n):
#         if (arr[i]-1 == last_smallest):
#             count_current += 1
#             last_smallest = arr[i]
#         elif (arr[i] != last_smallest):
#             count_current = 1
#             last_smallest = arr[i]
#         longest = max(longest, count_current)

#     return longest

# def main():
#     arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
#     print(LCSnum(arr))

# if __name__ == "__main__":
#     main()

'''----------------------------------------------------------------------------------------------------------------------------------'''

'''Optimal solution using set()'''
'''tc - O(3n) and sc - O(n)'''
def LCSnum(arr):
    n = len(arr)
    if n == 0: 
        return -1

    longest = 1
    hash_set = set(arr) 

    for i in hash_set:
        if (i - 1) not in hash_set:  
            current_count = 1
            value = i

            while (value + 1) in hash_set:  
                value += 1
                current_count += 1

            longest = max(longest, current_count)

    return longest

def main():
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    print(LCSnum(arr)) 

if __name__ == "__main__":
    main()