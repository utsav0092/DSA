def pattern(n):
    for i in range(n+1):
        ch = 69 #E
        for j in range(i):
            print(chr(ch), end="")
            ch = ch - 1 #E = E - 1 => D 
        print()

if  __name__ == "__main__":
    pattern(5)