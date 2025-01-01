def pattern(n):
    for i in range(n):
        #space
        for j in range(n - i - 1):
            print(" ", end="")
        #print
        ch = 65
        for j in range(2 * i + 1):
            print(chr(ch), end="")
            if j < i:
                ch += 1
            else:
                ch -= 1
        print()

if __name__ == "__main__":
    pattern(5)