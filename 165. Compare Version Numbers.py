"""
Approach:
    
    1. TC: O(N):
        
        a. Convert version strs into list by spliit('.')
        b. Loop for maxlen( va , vb )
        c. Ia = int(va[i]) if i < len(va) else take 0
           Ib = int(vb[i]) if i < len(vb) else take 0
           
        d. if Ia < Ib: return -1, if ia > ib: return 1
       return 0
       
     LeetCode 165: https://leetcode.com/problems/compare-version-numbers/
     YT: https://www.youtube.com/watch?v=Nk0D58HRxfw
"""

class Solution:
    def compareVersion(self, va: str, vb: str) -> int:
        va = va.split('.')
        vb = vb.split('.')
        
        for i in range(max(len(va), len(vb))):
            
            ia = int(va[i]) if i < len(va) else 0
            ib = int(vb[i]) if i < len(vb) else 0
            
            if ia > ib: return 1
            if ia < ib: return -1
            
        return 0
            
