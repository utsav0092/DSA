'''Striver's logic'''
# class Solution():
#     def gcd(self, a, b):
#         for i in range(1, min(a, b)+1):
#             if a%i == 0 and b%i == 0:
#                 gcd = i
#         return gcd

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.gcd(5, 10)) # 5

'''GFG solution for finding LCM and GCD/HCF'''
class Solution():
    def gcdandlcm(self, a, b):
        l = []
        for i in range(1, min(a, b)+1):
            if a%i == 0 and b%i == 0:
                l.append(i)
        lcm = ((a*b)//max(l))
        l.append(lcm)
        return l

if __name__ == "__main__":
    sol = Solution()
    val = sol.gcdandlcm(5, 10)         
    print(val[1:])  