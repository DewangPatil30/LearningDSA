"""
3 Approaches:
    
    1. Nested loop count each ele freq: TC:O(n^2) 
    2. Use map and store each ele freq: TC: O(n) SC: O(n)
    
    3. Extended version of moories voting algo: 
        For n//3 there can be Atmost 2 elements with freq greater than n//3:
        
        So same as moories algo for n//2 we take 2 elements insteads of 1 than same as for n//2
        
    LeetCode 229: https://leetcode.com/problems/majority-element-ii/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b, ca, cb = -1, -1, 0, 0
        res = set()
        n = len(nums)
        
        for i in nums:
            if a == i: 
                ca += 1
            elif b == i: 
                cb += 1  
            elif ca == 0:
                a = i
                ca = 1
            elif cb == 0:
                b = i
                cb = 1
            else:
                ca -= 1
                cb -= 1
                
        ca , cb = 0, 0        
        
        for i in nums:
            if i == a: ca += 1
            if i == b: cb += 1
            
        if ca > n//3 and a not in res: res.add(a)
        if cb > n//3 and b not in res: res.add(b)
            
        return list(res)
            
