class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0



x = 3
y = 2
solution = Solution()
print(solution.divisorGame(x)) # False
print(solution.divisorGame(y)) # True