'''GFG print the number from 1 to n using recursion'''
class Recursion:
    def printNumber(self, n, count = 0):
        if count == n:
            return 
        else:
            print(count+1, end=" ")
            return self.printNumber(n, count+1)

if __name__ == "__main__":
    recursion = Recursion()
    num = int(input("Enter the number : "))
    recursion.printNumber(num)