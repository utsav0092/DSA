'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

def printPattern(n):
    """My logic"""
    # for i in range(1, 1+n):
    #     for j in range(i):
    #         print(f"{j+1}", end="")
    #     print()

    """His logic"""
    # for (i=1;i<=n;i++) {
    #     for (j=1;j<i;j++) {
    #         print("i")
    #     }
    #     print("\n")
    # }
    
if __name__ == "__main__":
    n = int(input("Enter the n : "))
    printPattern(n)