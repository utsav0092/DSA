'''GFG - Print the leaders in the array'''
'''tc - nearly O(n^2) and sc - O(n)'''

# def Leaders(arr):
#     n = len(arr)
#     ans = []
#     for i in range(n):
#         leader = True
#         for j in range(i+1, n):
#             if arr[j] > arr[i]:
#                 leader = False
#                 break
#         if leader == True:
#             ans.append(arr[i])
#     return ans

# def main():
#     arr = [12, 17, 4, 3, 5, 2]
#     print(Leaders(arr))

# if  __name__ == "__main__":
#     main()

'''Optimal solution'''
'''tc - O(n - with slicing the list in reverse) and sc - O(n)'''

# def Leaders(arr):
#     n = len(arr)
#     new_arr = []
#     maxx = float('-inf')
#     for i in range(n-1, -1, -1):
#         if arr[i] >= maxx:
#             new_arr.append(arr[i])
#             maxx = arr[i]
#     return new_arr[: : -1]
    
# def main():
#     arr = [12, 17, 4, 3, 5, 2]
#     print(Leaders(arr))

# if  __name__ == "__main__":
#     main()