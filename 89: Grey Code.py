"""
Approach: 
  
  1. for 2 it is [00,01,11,10]...........for 3 it is [000, 001, 111, 010, 110, 111, 101, 100]
      so the pattern is -- for n (eg. n=3) -> first just add 0 onto the n-1 array in left to right order
      than add 1 to n-1 array in right to left order 
      
      ie, for n=3:  [0+00, 0+01, 0+11, 0+10] left to right ------- [1+10, 1+11, 1+01, 1+00] and than combine thoes 2
      
  LeetCode 89: https://leetcode.com/problems/gray-code/
  YT: https://www.youtube.com/watch?v=Fha1CSxwvGg
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def manip(n):
            if n == 1:
                return ['0','1']
            
            x = manip(n-1)
            
            res = []
            for i in range(len(x)):
                res.append('0'+x[i])
            
            for i in range(len(x)-1, -1, -1):
                res.append('1'+x[i])
                
            return res
        
        
        new = []
        bits = manip(n)
        for i in bits:
            new.append(int(i, 2))
            
        return new
      
      
