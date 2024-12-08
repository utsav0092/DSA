class Solution:
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canDistribute(max_bag_size):
            """
            Helper function to check if it's possible to ensure all bags have size <= max_bag_size 
            using at most maxOperations.
            """
            operations = 0
            for num in nums:
                # Calculate required splits for current bag
                if num > max_bag_size:
                    operations += (num - 1) // max_bag_size
            # Check if total operations are within allowed limit
            return operations <= maxOperations

        # Binary search for the minimum possible maximum size
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                # If possible to distribute with this size, try smaller sizes
                right = mid
            else:
                # If not possible, increase the size
                left = mid + 1
        return left

# Example usage
if __name__ == "__main__":
    nums = [9, 7, 2]  # Example input
    maxOperations = 2  # Example max operations
    solution = Solution()
    print(solution.minimumSize(nums, maxOperations))  # Output the result
