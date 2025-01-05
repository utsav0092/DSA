'''Find all the divisors of a number by striver'''
# def printDivisiors(n):
#     l = []
#     for i in range(n**0.5):
#         if (n%i == 0):
#             l.append(i)
#             if (n//i!=i):
#                 val = n//i
#                 l.append(val)
#     l.sort()
#     return l

# if __name__ == '__main__':
#     n = 100
#     print(printDivisiors(n))


'''GFG solution for finding divisors of a number'''
class Solution:
    def sumOfDivisors(self, n):
        # Initialize the total sum
        total_sum = 0

        # Calculate the sum of divisors for each number from 1 to n
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    total_sum += j
                    if j != i // j:  # Add the complementary divisor if it's different
                        total_sum += i // j

        return total_sum


# Example usage
if __name__ == "__main__":
    n = 4  # Input
    ob = Solution()
    print("Output:", ob.sumOfDivisors(n))
