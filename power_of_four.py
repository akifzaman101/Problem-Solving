class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        count = 0
        while n % 2 == 0:
            n //= 2
            count += 1

        if n != 1:
            return False

        if count % 2 == 0:
            return True
        else:
            return False


#Example Usage:
solution = Solution()
print(solution.isPowerOfFour(16))  # True
print(solution.isPowerOfFour(5))   # False
print(solution.isPowerOfFour(1))   # True
