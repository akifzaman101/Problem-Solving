class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        cur_end = 0
        cur_farthest = 0
        
        for i in range(n - 1):

            if i + nums[i] > cur_farthest:
                cur_farthest = i + nums[i]
            

            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest
        
        return jumps


# Example usage:
solution = Solution()
print(solution.jump([2,3,1,1,4]))  # Output: 2
print(solution.jump([2,3,0,1,4]))  # Output: 2
