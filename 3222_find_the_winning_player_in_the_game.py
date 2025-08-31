class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        
        if x % 2 == 0:
            return "Bob"
        else:
            return "Alice"


##Example usage:
solution = Solution()
print(solution.winningPlayer(2, 7))  # Alice
print(solution.winningPlayer(4, 11)) # Bob