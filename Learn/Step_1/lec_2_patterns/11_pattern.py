def pattern(n):
    for i in range(1, n + 1):  # Start from 1 to print the pattern correctly
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i):
            print(start, end=" ")  # Use end=" " for horizontal printing
            start = 1 - start  # Toggle between 1 and 0
        print()  # Move to the next line after each row

if __name__ == "__main__":
    pattern(5)