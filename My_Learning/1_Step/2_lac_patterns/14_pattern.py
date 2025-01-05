def print_pattern(n):
    for i in range(1, n + 1):  # Loop through rows
        for j in range(65, 65 + i):  # Loop through characters (ASCII value of 'A' is 65)
            print(chr(j), end="")  # Convert ASCII to character
        print()  # Move to the next line after each row

if __name__ == "__main__":
    print_pattern(5)
