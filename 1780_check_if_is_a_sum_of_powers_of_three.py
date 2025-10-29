class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
            
                
                
            
            


        
        
#Example Usage:
solution = Solution()
print(solution.checkPowersOfThree(12))
print(solution.checkPowersOfThree(91))
print(solution.checkPowersOfThree(21))
                
                
            