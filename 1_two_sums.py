from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i,num in enumerate(nums):
            j = target - num
            if j in dict:
                return [dict[j],i]
            dict[num] = i
            

solution = Solution()
print(solution.twoSum([2, 7, 3, 6], 9))  # [0, 1]
print(solution.twoSum([3, 2, 4], 6))     # [1, 2]
print(solution.twoSum([3, 3], 6))        # [0, 1]