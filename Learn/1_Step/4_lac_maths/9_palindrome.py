def isPalindrome(x):
    y =  x < 1
    x = abs(x)

    temp = x
    rev = 0
    n = 0
    while temp > 0:
        n = temp % 10
        rev = rev*10 + n
        temp = temp // 10
        
    if y:
        rev = -rev
        
    if rev == x:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(isPalindrome(12321))