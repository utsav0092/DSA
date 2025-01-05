def armstrongNumber (n):
    temp = n
    div = 0
    d = 0
    while temp > 0:
        d = temp % 10
        div = div + d**3
        temp = temp // 10
    if div == n:
        return True
    else:
        return False

if __name__ == "__main__":
    print(armstrongNumber(123))