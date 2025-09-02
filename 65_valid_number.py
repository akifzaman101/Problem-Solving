class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if len(s) == 0:
            print("Empty string after strip")
            return False
        
        invalid_char_lst = [
            "+-", "++", "--", "-+", "e.", "ee", "eE", "-.","+.",".+",".-",
            "E.", "EE", "Ee", "..", "e+", "e-", "E+", "E-", "+e", "-e", "+E", "-E"
        ]
        digit_count = 0
        dot_count = 0
        letter_count = 0
        e_count = 0
        symbol_count = 0
        
        for char in s:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():
                if char != "e" and char != "E":
                    letter_count += 1
                else:
                    e_count += 1
            elif char == '.':
                dot_count += 1
            elif char == '+' or char == '-':
                symbol_count += 1
            else:
                return False
                
        
        
        if digit_count == 0 or dot_count > 1 or e_count > 1 or letter_count > 0 or symbol_count > 2:
            return False

  
        for i in range(len(s)):
            
            if s[i] == '+' or s[i] == '-':
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                if i == 0 and s[i+1] == "." and s[i+2] != "e" and s[i+2] != "E":
                    return True
                
            if s[i] == ".":
                if i <= len(s) and i == 0 and s[i+1] == "e":
                    return False 
            
            if s[i] == 'e' or s[i] == 'E':
                if i==0 or i==len(s)-1: 
                    return False
                if len(s) <= 3 and s[i-1] == ".":
                    return False
                if "." in s[i+1:]:
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
# print(solution.isNumber("e1")) # False
# print(solution.isNumber("-1E+3")) # True
# print(solution.isNumber("0e")) # False
print(solution.isNumber("+E3")) # False
print(solution.isNumber("46.e3")) # true
print(solution.isNumber("46.e3")) # true
print(solution.isNumber(".e1")) # False
print(solution.isNumber("+.8")) # True
print(solution.isNumber("-.E3")) # False
print(solution.isNumber("6e6.5")) # False
print(solution.isNumber(".e132")) # False








