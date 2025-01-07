'''Print the factorial of the n number using recursion'''
class Recursion:
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

if __name__ == "__main__":
    recursion = Recursion()
    num = int(input("Enter the number: "))
    print(f"The factorial is: {recursion.factorial(num)}")

'''GFG solution'''
