'''Check if the string is palindrome or not? Striver's code'''
class Recursion:
    def pali(self, name, i = 0):
        n = len(name)
        if (i >= n // 2):
            return True
        if (name[i] != name[n-i-1]):
            return False
        else:
            return self.pali(name, i+1)

if __name__ == "__main__":
    r = Recursion()
    name = input("Enter a string: ")
    print(r.pali(name))

'''Leetcode problem all test cases passed but not submitted'''
import string
class Solution:
    def isPalindrome(self, s: str, i = 0) -> bool:
#Removes the punchuations from the string
        s = ''.join([char for char in s if char not in string.punctuation])  
#Converts to lower case and remove the spaces from the string
        s = s.replace(" ", "").lower()
        n = len(s)
        if (n>0):
            if (i >= n//2):
                return True
            if (s[i] != s[n-i-1]):
                return False
            else:
                return self.isPalindrome(s, i+1)
        else:
            return True

'''Leet code Valid palindrome using loop optimised solution'''
import string
class Solution:
    def isPalindrome(self, s):
        # Remove punctuation and spaces, and convert to lowercase
        s = ''.join([char for char in s if char not in string.punctuation])
        s = s.replace(" ", "").lower()
    
        # Check for palindrome
        return s == s[::-1]

if __name__ == "__main__":
    r = Solution()
    print(r.isPalindrome("A man, a plan, a canal: Panama")) 

'''Leet code valid palindrome using recursion solution'''
import string

class Solution:
    def isPalindrome(self, s):
        # Helper function to remove punctuation and spaces
        def cleanString(s):
            s = ''.join([char for char in s if char not in string.punctuation])
            return s.replace(" ", "").lower()

        # Recursive function to check for palindrome
        def checkPalindrome(s, left, right):
            if left >= right:  # Base case: if the pointers meet or cross, it's a palindrome
                return True
            if s[left] != s[right]:  # If characters at pointers don't match, not a palindrome
                return False
            return checkPalindrome(s, left + 1, right - 1)  # Recursive call with updated pointers

        # Clean the string and initialize recursion
        s = cleanString(s)
        return checkPalindrome(s, 0, len(s) - 1)

# Example usage
if __name__ == "__main__":
    r = Solution()
    print(r.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(r.isPalindrome("race a car"))                     # Output: False