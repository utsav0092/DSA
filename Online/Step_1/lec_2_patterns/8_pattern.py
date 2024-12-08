"""

"""

def pattern(n):
    for i in range(0, n):
        '''space'''
        for j in range(0, n):
            print(" ", end="")
        '''star'''
        for j in range(0, 2*n-(2*i+1)):
            print("*", end="")
        '''space'''
        for j in range(0, n):
            print(" ", end="")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number : "))
    pattern(n)