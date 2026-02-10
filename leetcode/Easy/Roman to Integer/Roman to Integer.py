class Solution(object):
    def romanToInt(self, s):
        
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0

        for x in range(len(s)-1):
            if roman[s[x]] < roman[s[x+1]]:
                total -= roman[s[x]]
            else:
                total += roman[s[x]]
        # total += roman[s[len(s)-1]]
        total += roman[s[-1]]

        return total

# Faster

# class Solution(object):
#     def romanToInt(self,s):
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         result = 0
#         prev_value = 0
        
#         for char in reversed(s):
#             curr_value = roman_map[char]
#             if curr_value < prev_value:
#                 result -= curr_value
#             else:
#                 result += curr_value
#             prev_value = curr_value
        
#         return result