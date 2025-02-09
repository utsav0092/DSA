'''Leetcode - 2 sum problem'''

def twoSum(arr, k):
    n = len(arr)
    i = 0
    j = 0
    while (i < n):
        while (j < n):
            if arr[i] + arr[j] == k:
                return arr[i], arr[j]
            else:
                j += 1
        i += 1

def main():
    arr = [1,2,3,4,5]
    k = 6
    print(twoSum(arr, k))

if __name__ == "__main__":
    main()