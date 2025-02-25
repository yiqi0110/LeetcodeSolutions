# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

#     1. Whitespace: Ignore any leading whitespace (" ").
#     2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#     3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached.
#         If no digits were read, then the result is 0.
#     4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. 
#         Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

# Return the integer as the final result.

class Solution:
    def myAtoi(self, s: str) -> int:
        valueAsStr = ""
        isNegative = None
        checkNext = False
        if len(s.lstrip()) == 0:
            return 0
        for i, c in enumerate(s.lstrip()):
            if i == 0:
                if c == "-":
                    isNegative = True
                    continue
                if c == "+":
                    isNegative = False
                    continue
            if c.isdigit() == False:
                print(i,c)
                if len(valueAsStr) == 0:  
                    return 0
                break
            if c.isdigit():
                valueAsStr += c
                continue
        if len(valueAsStr) == 0:
            return 0
        if isNegative:
            valueAsStr = "-" + valueAsStr
        val = int(valueAsStr)
        if val < -2**31:
            val = -2**31
        elif val > 2**31-1:
            val = 2**31-1

        return val