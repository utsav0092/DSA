def pattern(n):
    for i in range(n, 1, -1):  # Loop through rows
        for j in range(65, 65 + i):  # Loop through characters in reverse
            print(chr(j), end="")  # Convert ASCII to character
        print()  # Move to the next line after each row

if __name__ == "__main__":
    pattern(5)