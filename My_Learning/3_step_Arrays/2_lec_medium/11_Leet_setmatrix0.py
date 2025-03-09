'''Leetcode - Set Matrix Zero (column wise and row wise)'''
'''Brute force'''
'''tc - O(n*m * (n+m)) and sc - O()'''

# def SMZ(arr):
#     n = len(arr)
#     m = len(arr[0])

#     # First pass: Mark the rows and columns that need to be changed
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0:
#                 markRow(i, m, arr)
#                 markCol(j, n, arr)
#     return arr

# def markRow(i, m, arr):
#     for j in range(m):
#         if arr[i][j] != 0:  # Keep original zeroes intact
#             arr[i][j] = -1

# def markCol(j, n, arr):
#     for i in range(n):
#         if arr[i][j] != 0:  # Keep original zeroes intact
#             arr[i][j] = -1

# def main():
#     arr = [
#         [1, 1, 1, 1],
#         [1, 0, 0, 1],
#         [1, 1, 1, 1],
#     ]
#     result = SMZ(arr)
#     for row in result:
#         print(row)

# if __name__ == "__main__":
#     main()


'''Better solution'''
'''tc - O(2*n*m) and sc - O(n) + O(m)'''

# def zeroMatrix(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
#     row = [0] * n 
#     col = [0] * m 

#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 row[i] = 1
#                 col[j] = 1

#     for i in range(n):
#         for j in range(m):
#             if row[i] or col[j]:
#                 matrix[i][j] = 0

#     return matrix

# def main():
#     matrix = [[1, 1, 1], 
#               [1, 0, 1], 
#               [1, 1, 1]]

#     ans = zeroMatrix(matrix)

#     print("The Final matrix is:")
#     for row in ans:
#         for ele in row:
#             print(ele, end=" ")
#         print()

# if __name__ == "__main__":
#     main()  

'''Optimal solution'''
'''tc - O() and sc - O()'''

def SMZ(arr):
    n = len(arr)
    m = len(arr[0])
    return arr

def main():
    matrix = [[1, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]]

    ans = SMZ(matrix)

    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()

if __name__ == "__main__":
    main()  