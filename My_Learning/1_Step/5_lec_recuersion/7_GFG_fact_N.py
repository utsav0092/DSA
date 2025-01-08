'''Print the factorial of the N number using recursion'''
class Recursion:
    def factNumber(self, n):
        if n == 1:
            return 1
        else:
            return (n * self.factNumber(n-1))

if __name__ == "__main__":
    o = Recursion()
    num = int(input("Enter the number : "))
    print(o.factNumber(num))

'''GFG solution'''