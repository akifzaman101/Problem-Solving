class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ['(','[','{']
        parenthesis_map = {')':'(',
                           ']':'[',
                           '}':'{'}
        stack = []
        
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == parenthesis_map[char]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0
    
            
        
    


##Example usage:
solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))