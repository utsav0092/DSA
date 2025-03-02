'''Leetcode - find the maximum subarray sum'''
'''TC - O(n^3) and SC - O(1)'''

# def kadane(arr):
#     n = len(arr)
#     maxx = float('-inf')
#     for i in range(n):
#         for j in range(i, n):
#             summ = 0
#             for k in range(i, j):
#                 summ += arr[k]
#                 maxx = max(maxx, summ)
#     return maxx

# def main():
#     arr = [-2,-3,4,-1,-2,1,5,-3]
#     print(kadane(arr))

# if __name__ == "__main__":
#     main()

'''Better solution'''
'''TC - O() and SC - O()'''

# def kadane(arr):
#     n = len(arr)
#     maxx = float('-inf')
#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             summ += arr[j]
#             maxx = max(maxx, summ)
#     return maxx

# def main():
#     arr = [-2,-3,4,-1,-2,1,5,-3]
#     print(kadane(arr))

# if __name__ == "__main__":
#     main()

'''Optimised solution using (Kadane's algo maximun sum) returns the sum'''
'''TC - O(n) and SC - O(1)'''

# def kadane(arr):
#     n = len(arr)
#     maxSum = float('-inf')
#     currSum = 0
#     for i in range(n):
#         currSum += arr[i]
#         maxSum = max(maxSum, currSum)
#         if currSum < 0:
#             currSum = 0
#     return maxSum

# def main(): 
#     arr = [-3,-4,-5,-4,-1,-7,-8]
#     print(kadane(arr))

# if __name__ == "__main__":
#     main()

'''returns the maximun sum subarray [...]'''

def kadane(arr):
    n = len(arr)
    maxSum = float('-inf')
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    return maxSum

def main(): 
    arr = [3,-4,5,4,-1,7,-8]
    print(kadane(arr))

if __name__ == "__main__":
    main()