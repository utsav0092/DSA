'''GFG - Longest subarray with sum k'''
'''Brute force solution tc - O(n^3) and sc - O(1)'''

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

'''Better apraoch'''
'''tc - O() and sc - O()'''

def subArray(arr, k):
    n = len(arr)
    return n

def main():
    arr = [1,2,3,4,5]
    k = 5
    print(subArray(arr, k))

if __name__ == "__main__":
    main()