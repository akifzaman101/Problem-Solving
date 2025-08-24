from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


nums = [3,2,2,3]
val = 3

solution = Solution()
j = solution.removeElement(nums,val)
print("output:", j)
print("nums = ", nums[:j])
