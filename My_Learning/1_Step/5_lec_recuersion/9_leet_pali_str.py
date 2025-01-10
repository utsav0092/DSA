'''Check if the string is palindrome or not?'''
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

'''Leetcode problem all test cases passed but not submitted yet'''
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