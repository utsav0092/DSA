"""
    *
   ***
  *****
 *******
*********

"""

def pattern(n):
    '''outer loop'''
    for i in range(0, n):
        '''space'''
        for j in range(0, n-i-1):
            print(" ", end="")
        '''start'''
        for j in range(0, 2*i+1):
            print("*", end="")
        '''space'''
        for j in range(0, n-i-1):
            print(" ", end="")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number : "))
    pattern(n)   