'''Print the name 5 times without using loop'''
# class Recursion:
#     def printName(self, n, name):
#         if n == 0:
#             return 0
#         else:
#             print(name, end=" ")
#             return n + self.printName(n-1, name)

# if __name__ == "__main__":
#     recursion = Recursion()
#     name = input("Enter the name : ")
#     num = int(input("Enter the number : "))
#     recursion.printName(num, name)

'''GFG print the number from 1 to n using recursion'''
# class Recursion:
#     def printNumber(self, n, count = 0):
#         if count == n:
#             return 
#         else:
#             print(count+1, end=" ")
#             return self.printNumber(n, count+1)

# if __name__ == "__main__":
#     recursion = Recursion()
#     num = int(input("Enter the number : "))
#     recursion.printNumber(num)

'''GFG print the number from n to 1 using recursion'''
# class Recursion:
#     def printNumber(self, n):
#         if n == 0:
#             return 
#         else:
#             print(n, end=" ")
#             return self.printNumber(n-1)

# if __name__ == "__main__":
#     recursion = Recursion()
#     num = int(input("Enter the number : "))
#     recursion.printNumber(num)

'''GFG sum the number from 1 to n using recursion'''
# class Recursion:
#     def sum(self, n):
#         if n == 0:  
#             return 0
#         else:  
#             return n + self.sum(n - 1)

# if __name__ == "__main__":
#     recursion = Recursion()
#     num = int(input("Enter the number: "))
#     print("The sum is:", recursion.sum(num))

'''GFG print the factorial of the n number using recursion'''
# class Recursion:
#     def factorial(self, n):
#         if n == 0:
#             return 1
#         else:
#             return n * self.factorial(n - 1)

# if __name__ == "__main__":
#     recursion = Recursion()
#     num = int(input("Enter the number: "))
#     print(f"The factorial is: {recursion.factorial(num)}")