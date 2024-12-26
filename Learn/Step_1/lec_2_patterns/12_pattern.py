def pattern(n):
    space = 2 * (n - 1)  # Initialize space for the first row
    for i in range(1, n + 1):
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print spaces
        for j in range(space):
            print(" ", end="")
        
        # Print decreasing numbers
        for j in range(i, 0, -1):
            print(j, end="")
        
        print()  # Move to the next line
        space -= 2  # Reduce space by 2 for the next row

if __name__ == "__main__":
    pattern(5)