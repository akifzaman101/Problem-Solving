from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return "invalid!"
        
        first_index_value = strs[0]
        for i in strs[1:]:
            while i[:len(first_index_value)] != first_index_value:
                first_index_value = first_index_value[:-1]
                
                if not first_index_value:
                    return ""
        return first_index_value
                

strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
            