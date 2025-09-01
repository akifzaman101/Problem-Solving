class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            print("Empty string after strip")
            return False
        
        invalid_char_lst = [
            "+-", "++", "--", "-+", ".e", "e.", "ee", "eE",
            ".E", "E.", "EE", "Ee", "..", "e+", "e-", "E+", "E-", "+.", "-."
        ]
        has_digit = False
        
        for char in s:
            if char.isdigit():
                has_digit = True 
            elif char.isalpha():
                if char != "e" and char != "E":
                    return False
        
        
        if has_digit == False:
            return False

  
        for i in range(len(s)):
            
            if s[i] == 'e' or s[i] == 'E':
                if s[i+1].isdigit() or s[i-1].isdigit():
                    return False
           
            value = s[i:i+2]
            if value == "e+" or value == "e-" or value == "E+" or value == "E-":
                if i+2 < len(s):
                    if s[i+2].isdigit() == False and  s[i-1].isdigit() == False:
                        return False
                    else:
                        return True
                    
            if value in invalid_char_lst:
                print(f"Invalid pair found: {value}")
                return False
        
        return True
        
        
       

#Example usage:
solution = Solution()
# print(solution.isNumber("0"))
# print(solution.isNumber(" 0.1 "))
# print(solution.isNumber("abc"))
# print(solution.isNumber("1 a"))
# print(solution.isNumber("2e10"))
# print(solution.isNumber(" -90e3+   "))
print(solution.isNumber("e1"))
print(solution.isNumber("-1E+3"))
print(solution.isNumber("0e"))

