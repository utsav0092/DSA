def pattern(n):
    spaces = 2 * n - 2
    for i in range(1, 2 * n):
        # Determine the number of stars
        if i <= n:
            stars = i
        else:
            stars = 2 * n - i
        
        # Print stars
        for j in range(stars):
            print("*", end="")
        
        # Print spaces
        for j in range(spaces):
            print(" ", end="")
        
        # Print stars
        for j in range(stars):
            print("*", end="")
        
        # Adjust spaces
        if i < n:
            spaces -= 2
        else:
            spaces += 2
        
        print()

if __name__ == "__main__":
    pattern(5)