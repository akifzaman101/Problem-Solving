class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
            
        return True
    
#Example Usage:
solution = Solution()
print(solution.isPowerOfTwo(1))   # True
print(solution.isPowerOfTwo(16))  # True
print(solution.isPowerOfTwo(3))   # False