'''
* * * *
* * * *
* * * * 
* * * * 
'''

def printPattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ") 
        print() 

if __name__ == "__main__":
    n = int(input("Enter the number of lines you want : "))
    printPattern(n)