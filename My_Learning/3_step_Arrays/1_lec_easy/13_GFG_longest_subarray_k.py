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

'''Better apraoch (prefixsum algorithm)'''
'''tc - O() and sc - O()'''

def subArray(arr, k):
    n = len(arr)
    # first part of the problem
    prefixSum = []
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum

def main():
    arr = [1,2,3,4,5]
    k = 5
    print(subArray(arr, k))

if __name__ == "__main__":
    main()