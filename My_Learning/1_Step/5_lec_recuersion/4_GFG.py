'''GFG print the number from N to 1 using recursion'''
class Recursion:
    def printNumber(self, n):
        if n == 0:
            return 
        else:
            print(n, end=" ")
            return self.printNumber(n-1)

if __name__ == "__main__":
    recursion = Recursion()
    num = int(input("Enter the number : "))
    recursion.printNumber(num)