# '''Find the number that appears once and the others twice'''
# '''TC - O(n^2) and SC - O(n)'''

def appearOnce(nums):
    n = len(nums)
    for i in range(n):
        num = nums[i]
        count = 0
        for j in range(n):
            if num == nums[j]:
               count = count + 1
        if count == 1:
            return num
#-------------------------------- TC - O(n)
    n = list(set(nums))
    for x in n:
        l = [y for y in nums if y == x]
        if len(l) == 1:
            return x
            
def main():
    nums = [1,1,2,3,3,4,4]
    print(appearOnce(nums))

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------

'''Better solution using hashmap (key : value)'''
'''TC-O(n) and SC-O(1)'''  

def appearOnce(nums):
    n = len(nums)
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count == 1:
            return num

def main():
    nums = [4,1,2,1,2]
    print(appearOnce(nums))

if __name__ == "__main__":
    main()

#--------------------------------------------------------------------------------------

'''Most optimal solution using XOR operator''' 
def appearOnce(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor

def main():
    nums = [4,1,2,1,2]
    print(appearOnce(nums))

if __name__ == "__main__":
    main()