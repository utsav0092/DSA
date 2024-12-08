'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

def print_pattern(n):
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))

# Call the function with the desired number of rows
print_pattern(5)