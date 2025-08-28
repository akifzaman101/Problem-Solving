class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
           return 0
        return len(words[-1])
            

# Example usage:
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  
            