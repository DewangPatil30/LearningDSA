"""
My Approach :-

1. take a stack with -1 initial value so that if there is nothing it will evaluate length correct ie, i - indstaxk[-1] -> 1 - (-1) = 2
2. if s[i] is opening brac than append index of it else pop the top of stack
3. if after poping top, the stack is empty than closing brac was problemable so push its index in stack
4. else take the length as index (i - indstack[-1]) ie, currIndex - top of stack and compare to previous max.

LeetCode 32: https://leetcode.com/problems/longest-valid-parentheses/
YT: https://www.youtube.com/watch?v=G53_EUjUYcQ

"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        indstack = [-1]
        maxl, l = 0, 0
        
        for i in range(len(s)):
            
            if s[i] == '(':
                indstack.append(i)
            else:
                indstack.pop()
                if not indstack: indstack.append(i)
                else: maxl = max(maxl, (i - indstack[-1]))
                        
        return maxl
      
      
