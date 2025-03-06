'''Leetcode - Longest Common Subsequence'''
'''Brute solution'''
'''tc - O(n^2) and sc - O(n)'''

def LCSnum(arr):
    num_set = set(arr)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            count = 1

            while current_num + 1 in num_set:
                current_num += 1
                count += 1

            longest = max(longest, count)

    return longest

def main():
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    print(LCSnum(arr))  

if __name__ == "__main__":
    main()



'''Better solution'''
'''tc - O() and sc - O()'''

# def LCSnum(arr):
#     n = len(arr)

#     if not arr:
#         return 0
    
#     arr = sorted(set(arr)) 
#     longest = 1
#     current_streak = 1
#     for i in range(1, n):
#         if arr[i] == arr[i - 1] + 1:
#             current_streak += 1
#         else:
#             longest = max(longest, current_streak)
#             current_streak = 1

#     longest = max(longest, current_streak)
#     return longest
# def main():
#     arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
#     print(LCSnum(arr))

# if __name__ == "__main__":
#     main()