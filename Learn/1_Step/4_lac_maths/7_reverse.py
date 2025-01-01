def reverse(num):
        is_nag = num < 0
        num = abs(num)

        rev = 0
        while num > 0:
            rev = (rev*10) + (num%10)
            num = num // 10
        
        if is_nag:
            rev = -rev
        
        if rev < -2**31 or rev > 2**31-1:
            return 0

        return rev 

if __name__ == "__main__":
     print(reverse(-123)) 