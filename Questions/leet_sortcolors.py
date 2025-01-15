'''Leet code question for sorting the color'''
class Solution:
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] >= nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortColors([2,0,2,1,1,0]))