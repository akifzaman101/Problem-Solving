class Solution:
    def canWinNim(self, n: int) -> bool:
        
        return n % 4 != 0
    
    
##Example usage:
solution = Solution()
print(solution.canWinNim(4))
print(solution.canWinNim(1))
print(solution.canWinNim(2))
