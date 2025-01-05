'''My Solution for finding the Prime number'''
# class Solution():
#     def findPrime(self, n):
#         count = 0
#         N = n**0.5
#         for i in range(1, int(N+1)):
#             if n%i == 0:
#                 count += 1
#         if count > 2:
#             print(f"{n} is Not Prime")
#         else:
#             print(f"{n} is Prime")

# if __name__ == '__main__':
#     sol = Solution()
#     val = int(input("Enter the number: "))
#     sol.findPrime(val)

'''GFG Minimum Jumps required to react to the end of the array'''
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # If the array has only one element, no jumps are needed
        if n <= 1:
            return 0
        
        # If the first element is 0, we cannot move forward
        if arr[0] == 0:
            return -1
        
        # Initialize variables
        max_reach = arr[0]  # Maximum index we can reach
        steps = arr[0]      # Steps we can still take in the current jump
        jumps = 1           # Minimum number of jumps
        
        for i in range(1, n):
            # Check if we have reached the end of the array
            if i == n - 1:
                return jumps
            
            # Update the maximum reachable index
            max_reach = max(max_reach, i + arr[i])
            
            # Decrement the steps
            steps -= 1
            
            # If no steps are left
            if steps == 0:
                # Increment jump count
                jumps += 1
                
                # Check if the current index is beyond the maximum reachable index
                if i >= max_reach:
                    return -1
                
                # Reinitialize steps for the new jump
                steps = max_reach - i
        
        return -1  # If we haven't reached the end of the array

# Example usage
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
solution = Solution()
print(solution.minJumps(arr))  # Output: 3
# In the above example, the minimum number of jumps required to reach the end of the array is 3.
# We start at index 0 and jump to index 1 (1 jump).
# Then, we jump from index 1 to index 3 (2 jumps).
# Finally, we jump from index 3 to the end of the array (3 jumps).
# Note: The array elements represent the maximum number of steps we can take from that index.