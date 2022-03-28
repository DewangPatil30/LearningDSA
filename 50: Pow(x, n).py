"""
2 Approaches:
    
    1. Linear Iteration: multiply x with itself n times
        TC: O(n)
    
    2. Divide And Conquor: run while n > 0, if n is odd than [res *= x, n -= 1] else [x *= x, n = n//2], return res
        TC: O(log n)
    
    LeetCode 50: https://leetcode.com/problems/powx-n/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0: return 1
        nege = False
        
        if n < 0: 
            nege = True
            n *= -1
        
        res = 1
        while n:
            if n % 2:
                res *= x
                n -= 1
            else:
                x *= x
                n = n//2
                
        if nege: return 1/res
        return res
            
        
