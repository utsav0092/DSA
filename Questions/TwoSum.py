"""Brute force TC = O(n^2)"""
def twoSum(t,i,j,arr):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if  array[i]+array[j] == target:
                print(f"{array[i]}:{array[j]}")
        j = j+1
    i = i+1

if __name__ == "__main__":
    array = [1, 1, 3, 4, 5]
    i = 0
    j = 0
    target = 7
    twoSum(target, i, j, array)