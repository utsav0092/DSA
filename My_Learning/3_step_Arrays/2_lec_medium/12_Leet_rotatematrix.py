'''Leetcode - Rotate the matrix by 90'''
'''tc - O(n^2) and sc - O(n^2)'''
'''Brute force'''

# def rotate(matrix):
#     n = len(matrix)
#     temp = [[0] * n for _ in range(n)]  
#     for i in range(n):
#         for j in range(n):
#             temp[j][(n-1)-i] = matrix[i][j]
#     return temp

# def main():
#     matrix = [[1, 2, 3, 4], 
#               [5, 6, 7, 8], 
#               [9, 10, 11, 12], 
#               [13, 14, 15, 16]]
              
#     result = rotate(matrix)

#     for row in result:  
#         print(row)  

# if __name__ == "__main__":
#     main()

'''Better solution / in-place / transpose => reverse'''
'''tc - O(n/2*n/2+n/2 = n^2) and sc - O(1)'''

# def rotate(matrix):
#     n = len(matrix)

#     #transpose the matrix
#     for i in range(n): # (n-1)
#         for j in range(i+1, n):
#             matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#     #reverse in the matrix
#     for i in matrix:
#         i.reverse()

#     return matrix

# def main():
#     matrix = [[1, 2, 3, 4], 
#               [5, 6, 7, 8], 
#               [9, 10, 11, 12], 
#               [13, 14, 15, 16]]
              
#     result = rotate(matrix)

#     for row in result:  
#         print(row)  

# if __name__ == "__main__":
#     main()