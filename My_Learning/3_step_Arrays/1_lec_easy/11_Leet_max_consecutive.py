'''Leetcode - Max consecutive ones'''
'''TC - O(n) and SC - O(1)'''

def maxCons(nums):
    n = len(nums)
    count = 0
    long = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            long = max(long, count)
        else:
            count = 0
    return long

def main():
    nums = [1,0,1,1,1,0]
    print(maxCons(nums))

if __name__ == "__main__":
    main()