"""My approch"""
# def Reverse(num):
#     rev = 0
#     a = 0
#     while num > 0:
#         a = num % 10
#         rev = rev * 10 + a
#         num = num // 10
#     return rev

# if __name__ == "__main__":
#     num = int(input("Enter a number: "))
#     result = Reverse(num)
#     print(result)

"""Original"""
def reverse(num: int) -> int:
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
    result = reverse(input("Enter the value: "))
    print(result) 