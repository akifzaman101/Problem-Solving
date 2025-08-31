class Solution:
    def intToRoman(self, num: int) -> str:
        integer_to_roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        splited_numbers = []
        place = 1
        while num > 0:
            splitted_digit = (num % 10) * place
            if splitted_digit != 0:
                splited_numbers.append(splitted_digit)
            num //= 10
            place *= 10
        splited_numbers.reverse()
        print(splited_numbers)

        roman_number = ""
        for number in splited_numbers:
            if number in integer_to_roman_dict:
                roman_number += integer_to_roman_dict[number]
            else:
                keys = sorted(integer_to_roman_dict.keys())   

                previous_key = 0
                i = 0

                while i<len(keys) and keys[i] < number:
                    i += 1
                    
                
                if i == 0:  
                    previous_key = keys[0]
                elif i >= len(keys):  
                    previous_key = keys[-1]
                    value = number // previous_key
                    roman_number += integer_to_roman_dict[previous_key] * value
                else:  
                    previous_key = keys[i-1]
                    value = number 
                    while value > 0:
                        for k in reversed(keys):  
                            if k <= value:
                                roman_number += integer_to_roman_dict[k]
                                value -= k
                                break
                    
        return roman_number
                

##Example usage:
solution = Solution()
# print(solution.intToRoman(3))      # Output: "III"  
# print(solution.intToRoman(4))      # Output: "IV"
# print(solution.intToRoman(9))      # Output: "IX"
# print(solution.intToRoman(58))     # Output: "LVIII"
# print(solution.intToRoman(1994))   # Output: "MCMXCIV"
print(solution.intToRoman(3749))