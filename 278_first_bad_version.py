def isBadVersion(version):
    raise NotImplementedError

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
       left = 0
       right = n
       while left < right:
           mid = left + (right - left) // 2
           if isBadVersion(mid):
               right = mid
           else:
               left = mid + 1
       return left


# Example usage:
solution = Solution()
print(solution.firstBadVersion(5))  # Output: 4