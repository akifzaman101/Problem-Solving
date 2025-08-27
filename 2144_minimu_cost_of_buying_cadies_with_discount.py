from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total_cost = 0
        
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        
        return total_cost
    
print(Solution().minimumCost([1,2,3]))  # Output: 5
print(Solution().minimumCost([6,5,7,9,2,2]))  # Output: 23
print(Solution().minimumCost([5,5]))  # Output: 10