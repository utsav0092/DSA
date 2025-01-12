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