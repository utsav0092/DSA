'''Leet code question of power of four using loop'''
class Solution:
    def powerOfFour(self, n):
        if (n <= 0):
            return False
        while (n > 1):
            if (n%4 == 0):
                n = n // 4
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.powerOfFour(16)) 

'''Leet code question of power of four using recursion'''
class PowerOfFour:
    def check(self, n):
        if (n <= 0):
            return False
        if (n == 1):
            return True
        if (n%4 != 0):
            return False
        return self.check(n//4)

if __name__ == "__main__":
    p = PowerOfFour()
    print(p.check(16))