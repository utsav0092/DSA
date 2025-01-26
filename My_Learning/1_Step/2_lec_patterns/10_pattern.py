def pattern(n):
    for i in range(1, (2 * n)):
        if i <= n:  # Top part of the pattern
            stars = i
        else:       # Bottom part of the pattern
            stars = (2 * n - i)
        for j in range(stars):
            print("*", end="")
        print()  # Move to the next line

if __name__ == "__main__":
    pattern(5)