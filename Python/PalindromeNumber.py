# Given an integer x, return true if x is a , and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = [int(c) for c in str(x)]
        digitsCopy = digits.copy()
        digits.reverse()

        return digits == digitsCopy