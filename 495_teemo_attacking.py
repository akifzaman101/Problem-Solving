from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0
        for i in range(len(timeSeries) - 1):
            
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        
        total += duration
        return total
    
# Example usage:
solution = Solution()
print(solution.findPoisonedDuration([1,4], 2))  # Output: 4
print(solution.findPoisonedDuration([1,2], 2))  # Output: 3
            
            