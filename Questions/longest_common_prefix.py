class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Edge case: Empty input list
        if not strs:
            return ""
        
        # Sort the list of strings
        strs.sort()
        
        # Get the first and last string after sorting
        first = strs[0]
        last = strs[-1]
        
        # Initialize result to collect the common prefix
        result = []
        
        # Find the common prefix between the first and last string
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            result.append(first[i])  # Append matching characters to result
        
        # Return the result as a string
        return "".join(result)

# Example usage
solution = Solution()
strs = ["flow", "flower", "flowyer"]
print(solution.longestCommonPrefix(strs))
