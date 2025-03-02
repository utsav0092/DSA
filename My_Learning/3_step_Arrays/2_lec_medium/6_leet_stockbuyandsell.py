'''Leetcode - DP on stocks, Best time to buy and sell stocks'''
'''tc - O(n) and sc - O(1)'''

# def stock(nums):
#     n = len(nums)
#     profit = 0
#     minn = nums[0]
#     for i in range(1, n):
#         minn = min(minn, nums[i])
#         profit = max(profit, nums[i] - minn)
#     return profit
        
# def main():
#     arr = [7, 1, 5, 3, 6, 4]
#     print(stock(arr))

# if __name__ == "__main__":
#     main()

'''Striver's code'''

# def stock(prices):
#     n = len(prices)
#     profit = 0
#     minn = prices[0]
#     for i in range(1, n):
#         cost = prices[i] - minn
#         profit = max(profit, cost)
#         minn = min(minn, prices[i])
#     return profit

# def main():
#     arr = [7, 1, 5, 3, 6, 4]
#     print(stock(arr))

# if __name__ == "__main__":
#     main()