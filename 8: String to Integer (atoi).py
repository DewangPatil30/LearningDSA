"""
LeetCode: https://leetcode.com/problems/string-to-integer-atoi/
YT: https://www.youtube.com/watch?v=qxIprnPrVZA
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        nege = False
        res = 0
        s = s.strip()

        if not s: return 0
        
        if s[0] == '-': nege = True
        elif s[0] == '+': nege = False
            
        elif not s[0].isdigit(): return 0
        else: res = ord(s[0]) - ord("0")
        
        for i in range(1, len(s)):
            if s[i].isdigit():
                res = res*10 + (ord(s[i]) - ord("0"))
                
                if nege and res >= 2147483648: return -2147483648
                if not nege and res >= 2147483647: return 2147483647
                
            else: break
                
        if nege: return -res
        return res
      
      
