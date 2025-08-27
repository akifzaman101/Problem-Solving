class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count = 0
        for i in range(total // cost1 + 1):
            k = total - (i * cost1)
            count += k // cost2 + 1
        return count

print(Solution().waysToBuyPensPencils(20, 10, 5))  # Output: 9
print(Solution().waysToBuyPensPencils(5, 10, 10))