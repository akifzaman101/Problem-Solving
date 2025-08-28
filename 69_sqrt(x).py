class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left = 0
        right = x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left - 1 


# Example usage:
solution = Solution()
print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(8))  # Output: 2