'''Leet - find the missing number form the array'''
'''Brute force = TC - O(n^2) and SC - O(n)'''

def findMissing(nums, N):
    for i in range(1, N+1):
        flag = 0
        for j in range(len(nums)):
            if nums[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return -1

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    ans = findMissing(nums, N)
    print("The missing vallue is:", ans)

if __name__ == "__main__":
    main()

'''Optimised solution'''
'''TC - O(n) and SC - O(1)'''

def findMissing(arr):
    n = len(arr)
    e_sum = n * (n+1) // 2
    a_sum = sum(arr)
    missing = e_sum - a_sum
    if n > 1:
        return missing
    elif arr[0] == 0:
        return 1
    else:
        return 0
    #-------------------
    # arr = sorted(arr)
    # for i in range(len(arr)+1):
    #     if i not in arr:
    #         return i

def main():
    arr = [1,2,4]
    print(findMissing(arr))

if __name__ == "__main__":
    main()