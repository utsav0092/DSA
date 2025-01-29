class Solution:
    def evenlyDivides(self, n: int) -> int:
        count = 0  # Initialize a counter to keep track of divisible digits
        for digit in str(n):  # Convert n to a string to loop through each digit
            digit = int(digit)  # Convert the character back to an integer
            if digit != 0 and n % digit == 0:  # Check if digit is not 0 and divides n evenly
                count += 1  # If yes, increase the count
        return count  # Return the total count of divisible digits

if __name__ == "__main__":
    sol  = Solution()
    n = 12345
    print(sol.evenlyDivides(n)) # Output: 3