def pattern(n):
    space = 0
    for i in range(n):
        # First half: Top
        for j in range(n - i):  # Stars
            print("*", end="")
        for j in range(space):  # Spaces
            print(" ", end="")
        for j in range(n - i):  # Stars
            print("*", end="")
        space += 2
        print()
    
    space -= 2
    for i in range(n):
        # Second half: Bottom
        for j in range(i + 1):  # Stars
            print("*", end="")
        for j in range(space):  # Spaces
            print(" ", end="")
        for j in range(i + 1):  # Stars
            print("*", end="")
        space -= 2
        print()

if __name__ == "__main__":
    pattern(5)
