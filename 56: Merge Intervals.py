"""
2 Methods:-
  1. Use res = []: TC=O(nlogn) SC=O(n)
  2. Use original array: TC=O(nlogn) SC=O(1)
  
 in both, check if current interval's high range is greater eq to next interval's lower range than merge 
 else append next interval and than check for next interval

LeetCode 56: https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    def merge(self, intr: List[List[int]]) -> List[List[int]]:
        
        intr.sort(key=lambda x:x[0])
        i = 0
        l = len(intr)
        while i < l-1:
            if intr[i] > intr[i+1]:
                intr[i], intr[i+1] = intr[i+1], intr[i]
                
            if intr[i][1] >= intr[i+1][0]:
                intr[i][0] = min(intr[i][0], intr[i+1][0])
                intr[i][1] = max(intr[i][1], intr[i+1][1])
                
                intr.pop(i+1)
                i -= 1
                
            l = len(intr)
                
            i += 1
            
        return intr

   ############################# Use Res array #########################
   
        intr.sort(key=lambda x: x[0])
        res = [intr[0]]
        
        i = 1
        j = 0
        while i < len(intr):
            if res[j][1] >= intr[i][0]:
                res[j][1] = max(intr[i][1], res[j][1])
                i += 1
            else:
                res.append(intr[i])
                j += 1
                i += 1
                
        return res
                
