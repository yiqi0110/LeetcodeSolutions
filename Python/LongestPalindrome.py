# Given a string s, return the longest in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        while size > 0:
            for i in range(0, len(s)-(size-1)):
                subs = s[i:size+i]
                if self.palindromic(subs):
                    return subs
            size -= 1
        return ""
    
    def palindromic(self, s: str) -> bool:
            for i in range(len(s)):
                if s[i] == s[-1-i]:
                    continue
                else:
                    return False
            return True    