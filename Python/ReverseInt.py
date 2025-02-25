# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = abs(x)
        revInt = str(x)[::-1]
        if isNegative:
            revInt = "-" + revInt
        revInt = int(revInt)
        if revInt not in range((-2**31), ((2**31) - 1)):
            return 0
        return revInt