'''GFG sum the number of first N numbers using recursion'''
class Recursion:
    def sum(self, n):
        if n == 0:  
            return 0
        else:  
            return n + self.sum(n - 1)

if __name__ == "__main__":
    recursion = Recursion()
    num = int(input("Enter the number: "))
    print("The sum is:", recursion.sum(num))