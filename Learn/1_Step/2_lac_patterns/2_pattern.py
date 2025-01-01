'''
*
* *
* * *
* * * *
* * * * *
'''

def printPattern(n):
    
    """My logic"""
    # for i in range(n):
    #     for j in range(i+1):
    #         print("* ", end="")
    #     print()

    """His logic"""
    # for i in range(n+1):
    #     for j in range(i):
    #         print("* ", end="")
    #     print()

if __name__ == "__main__":
    n = int(input("Enter the n : "))
    printPattern(n)