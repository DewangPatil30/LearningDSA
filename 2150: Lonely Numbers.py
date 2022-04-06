"""
Approach: 
    !. Use Map: TC:O(N) SC:O(N)
        a. store each distinct ele in map with frequency
        b travase in map if freq of ele is 1 and ele +- 1 not in m then res.append(ele)
        return res
    
    LeetCode 2150: https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
"""

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        m = {}
        
        for v in nums:
            if v not in m: m[v] = 0
            m[v] += 1
        
        res = []
        for ele in m:
            if m[ele] == 1 and ele-1 not in m and ele+1 not in m:
                res.append(ele)
                
        return res
                 
