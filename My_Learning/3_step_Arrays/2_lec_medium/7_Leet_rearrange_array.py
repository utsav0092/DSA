'''Leetcode - Rearrange the array elements by sign'''
'''tc - O(2n) and sc - O(n) (n/2 + n/2)'''
'''Brute force'''

# def reArrange(arr):
#     n = len(arr)
#     pos = []
#     neg = []
#     for i in range(n):
#         if arr[i] > 0:
#             pos.append(arr[i])
#         else:
#             neg.append(arr[i])
#     for i in range(n//2):
#             arr[2*i] = pos[i]
#             arr[2*i+1] = neg[i]
#     return arr

# def main():
#     arr = [-3, -2, 2, 5]
#     print(reArrange(arr))

# if __name__ == "__main__":
#     main()

'''Better solution (2 pointers)'''
'''tc - O(n) and sc - O(n)'''

# def reArrange(arr):
#     n = len(arr)
#     new_arr = [0] * n
#     pos = 0
#     neg = 1
#     for i in range(n):
#         if arr[i] > 0:
#             new_arr[pos] = arr[i]
#             pos += 2
#         else:
#             new_arr[neg] = arr[i]
#             neg += 2
#     return new_arr

# def main():
#     arr = [-3, -2, 4, 5]
#     print(reArrange(arr))

# if __name__ == "__main__":
#     main()


'''Varietion in this problem (no of pos != no of neg)'''
'''tc - O(2n) (n + n/2) and sc - O(n)'''

# def reArrange(arr):
#     n = len(arr)
#     pos = []
#     neg = []

#     for i in range(n):
#         if arr[i] > 0:
#             pos.append(arr[i])
#         else:
#             neg.append(arr[i])

#     if len(pos) > len(neg):
#         for i in range(len(neg)):
#             arr[2*i] = pos[i]
#             arr[2*i+1] = neg[i]
#         index = len(neg) * 2
#         for i in range(len(neg), len(pos)):
#             arr[index] = pos[i]
#             index += 1
#     else:
#          for i in range(len(pos)):
#             arr[2*i] = pos[i]
#             arr[2*i+1] = neg[i]
#          index = len(pos) * 2
#          for i in range(len(pos), len(neg)):
#             arr[index] = neg[i]
#             index += 1

#     return arr

# def main():
#     arr = [1,2,-3,-4,-5,-6,-7,-8]
#     print(reArrange(arr))

# if __name__ == "__main__":
#     main()