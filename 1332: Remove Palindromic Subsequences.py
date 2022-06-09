"""
Approach: 
        Read the question carefully.... it states you can delete 1 subsequence at ones and subsequence not nesserally be contageous ie Non Contag
        so we can delete all a's at ones and b's at next so max steps be 2 and if palindrome than 2

LeetCode 1332: https://leetcode.com/problems/remove-palindromic-subsequences/
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return 2
        return 1
      
      
