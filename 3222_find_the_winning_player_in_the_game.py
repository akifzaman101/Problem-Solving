class Solution:
    def winningPlayer(self, x: int, y: int) -> str:

        y = y//4

        if(x<y):
            value = x
        else:
            value = y

        if(value % 2 == 0):
            return "Bob"
        else:
            return "Alice"
        


##Example usage:
solution = Solution()
print(solution.winningPlayer(2, 7))  # Alice
print(solution.winningPlayer(4, 11)) # Bob
print(solution.winningPlayer(1, 1)) # Bob
print(solution.winningPlayer(1, 2)) # Bob