# '''Leetcode - Print the spiral matrix'''
# '''Brute force'''
# '''tc - O(m*n) and sc - O(n)'''

# def spiral(matrix):
#     result = []
#     right = len(matrix[0])
#     left = 0
#     top = 0
#     bottom = len(matrix)

#     while left < right and top < bottom:
#         # Traverse from left to right
#         for i in range(left, right):
#             result.append(matrix[top][i])
#         top += 1

#         # Traverse from top to bottom
#         for i in range(top, bottom):
#             result.append(matrix[i][right - 1])
#         right -= 1

#         if not (left < right and top < bottom):
#             break  # Break if the entire matrix is covered

#         # Traverse from right to left
#         for i in range(right - 1, left - 1, -1):
#             result.append(matrix[bottom - 1][i])
#         bottom -= 1

#         # Traverse from bottom to top
#         for i in range(bottom - 1, top - 1, -1):
#             result.append(matrix[i][left])
#         left += 1

#     return result

# def main():
#     matrix = [[1, 2, 3, 4],
#               [4, 5, 6, 7],
#               [7, 8, 9, 10],
#               [11, 12, 13, 14]]
    
#     result = spiral(matrix)

#     for res in result:
#         print(res, end=" ")
#     print()

# if __name__ == "__main__":
#     main()

'''--------------------------------------------------------------------------------------------------------------------------------'''
'''My solution'''
def spiral(arr):
    
    if len(arr) == 0 or len(arr[0]) == 0:
        print("Empty")
        return
    
    top = 0
    left = 0
    right = len(arr[0])
    bottom = len(arr)


    while top < bottom and left < right:
        for i in range(left, right):
            print(arr[top][i])
        top += 1
        for i in range(top, bottom):
            print(arr[i][right-1])
        right -= 1
        for i in range(right-1, left-1, -1):
            print(arr[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1, -1):
            print(arr[i][left])
        left += 1

arr = [[1, 2, 3],
       [8, 9, 4],
       [7, 6, 5]]

spiral(arr)