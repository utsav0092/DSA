'''Leet question for power of two using loop'''
class PowerOfTwo:
    def check(self, n):
        if (n <= 0):
            return False
        while(n > 1):
            if (n%2 != 0):
                return False
            else:
                n = n // 2
        return True

if __name__ == "__main__":
    p = PowerOfTwo()
    print(p.check(-16))

'''Leet question for power of two using recursion'''
class PowerOfTwo:
    def check(self, n):
        if (n <= 0):
            return False
        if (n == 1):
            return True
        if (n%2 != 0):
            return False
        return self.check(n//2)

if __name__ == "__main__":
    p = PowerOfTwo()
    print(p.check(16))