from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        last_index = len(digits) - 1
        
        for i in range(last_index, -1, -1):
            print(i)
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits

                
            
        
    
digits = [1,2,4,9,9]    
solution = Solution()
k = solution.plusOne(digits)
print(k)
            