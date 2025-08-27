class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
    
    
# Example usage:
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 2
print(solution.strStr("aaaaa", "bba"))  # Output: -1