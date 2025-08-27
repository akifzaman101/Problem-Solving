from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > len(nums) // 2:
                return num

print(Solution().majorityElement([3,2,3]))  # Output: 3
print(Solution().majorityElement([2,2,1,1,1,2,2]))  # Output: 2
print(Solution().majorityElement([2,2,1,1,1,2,2,4,4,4,4,4,4,4,4]))  # Output: 2