'''Fibonacci series using recursion'''
class Solution:
    def fib(self, n):
        if (n <= 1):
            return n
        last = self.fib(n-1)
        slast = self.fib(n-2)
        return last + slast

if __name__ == "__main__":
    r = Solution()
    print(r.fib(10))

'''Fibonacci series using loops'''
class Solution:
    def fib(self, n):
        if n <= 1:  
            return n
        else:
            a = 0
            b = 1
            for i in range(2, n + 1):  
                temp = b
                b = a + b
                a = temp
            return b

if __name__ == "__main__":
    r = Solution()
    print(r.fib(10))  