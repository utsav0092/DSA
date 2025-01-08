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

'''Print Using backtracking'''
class Recursion:
    def printNumber(self, i, n):
        if i <= 0:
            return 
        self.printNumber(i-1, n)
        print(i)

if __name__ == "__main__":
    o = Recursion()
    num = int(input("Enter your number : "))
    o.printNumber(num, num)