'''Print the name N times without using loop'''
class Recursion:
    def printName(self, n, name):
        if n == 0:
            return 0
        else:
            print(name, end=" ")
            return n + self.printName(n-1, name)

if __name__ == "__main__":
    recursion = Recursion()
    name = input("Enter the name : ")
    num = int(input("Enter the number : "))
    recursion.printName(num, name)