class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_number = int(str(x)[::-1])
        return reversed_number == x


solution = Solution()
x = 124
print(solution.isPalindrome(x))