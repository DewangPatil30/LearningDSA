"""
  Approach:
  
            1. Usind Sort lambda x[1]:    eg: [[1,2],[7,8],[4,5]]
                TC: O(N log N)      SC: O(1)
                
              a. sort array based on ending len of pair ie, last val of each pair
              b. than simple 2ptr travasal l,r = 0,1  if pair[r][1] > pair[l][0]
                    count += 1, l = r
              return count      
              
LeetCode 646: https://leetcode.com/problems/maximum-length-of-pair-chain/
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key = lambda x: x[1])
        n = len(pairs)
        if n < 2: return n
        
        l, r = 0, 1
        count = 1
        while r < n:
            if pairs[r][0] > pairs[l][1]:
                count += 1
                l = r
            r += 1
            
        return count
    
    
