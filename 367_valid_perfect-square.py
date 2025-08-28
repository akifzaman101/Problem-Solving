class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return False
        
        left = 0
        right = num
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return False
    
# Example usage:
solution = Solution()
print(solution.isPerfectSquare(16))  # Output: True
print(solution.isPerfectSquare(14))  # Output: False
        