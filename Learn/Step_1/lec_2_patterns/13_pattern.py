def pattern(n):
    count = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(count, end=" ")
            count += 1
        print()

if __name__ == "__main__":
    pattern(5)