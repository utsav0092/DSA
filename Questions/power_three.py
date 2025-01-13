'''Leet code question of power of three using loop'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n <= 0):
            return False
        while (n > 1):
            if (n%3 == 0):
                n = n//3
            else:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()   
    print(solution.isPowerOfThree(27)) 

'''Leet code question of power of three using recursion'''
class PowerOfThree:
    def check(self, n):
        if (n <= 0):
            return False
        if (n == 1):
            return True
        if (n%3 != 0):
            return False
        return self.check(n//3)

if __name__ == "__main__":
    p = PowerOfThree()
    print(p.check(16))