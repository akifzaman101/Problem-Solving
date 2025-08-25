from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone_dict ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            possible_letters = phone_dict[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res
    
    
    
solution = Solution()
print(solution.letterCombinations("23"))