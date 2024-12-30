def pattern(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2) - j
            down = (2*n-2) - i
            print(f"{n - min(min(top, down), min(left, right))} ", end="")
        print()

if __name__ == "__main__":
    pattern(4) 