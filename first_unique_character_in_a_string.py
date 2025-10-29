class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1       

        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        
        return -1
    
    
#Example Usage:
solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
print(solution.firstUniqChar("aabb"))