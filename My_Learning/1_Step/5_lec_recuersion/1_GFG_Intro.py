'''Basic start of the Recursion'''
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

if __name__ == "__main__":
    num = int(input("Enter the number : "))
    print(sum(num)) 

'''GFG print the number from 1 to n using recursion'''
class Recursion:
    def sum(self, n, count = 0):
        if count == n:
            return 
        else:
            print(count + 1, end=" ")
            self.sum(n, count + 1)

if __name__ == "__main__":
    recursion = Recursion()
    num = int(input("Enter the number : "))
    recursion.sum(num)