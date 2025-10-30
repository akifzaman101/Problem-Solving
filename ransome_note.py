class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        
        for char in magazine:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
                
        for char in ransomNote:
            if char in count and count[char] > 0:
                count[char] -= 1
            else:
                return False
        
        return True