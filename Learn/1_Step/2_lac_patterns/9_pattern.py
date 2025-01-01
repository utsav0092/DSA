def pattern1(n):
    '''outer loop'''
    for i in range(0, n):
        '''space'''
        for j in range(0, n-i-1):
            print(" ", end=" ")
        '''start'''
        for j in range(0, 2*i+1):
            print("*", end=" ")
        '''space'''
        for j in range(0, n-i-1):
            print(" ", end=" ")
        print()

def pattern2(n):
    for i in range(0, n):
        # Left spaces
        for j in range(0, i):
            print(" ", end=" ")
        # Stars
        for j in range(0, 2 * n - (2 * i + 1)):
            print("*", end=" ")
        # Right spaces
        for j in range(0, i):
            print(" ", end=" ")
        # Move to the next line
        print()

if __name__ == "__main__":
    n = int(input("Enter the number : "))
    pattern1(n)
    pattern2(n)