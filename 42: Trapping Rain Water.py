"""
Two Methods:-  eg: [0,1,0,2,1,0,1,3,2,1,2,1]

  1. **Using leftmax array and rightmax array  tc:O(n)  sc:O(n):**:-
     in this method we will make left left view max arrya from left or right ie, [0,1,1,2,2,2,2,3,3,3,3,3]
     Similarly, rightmax arrya from right to left ie, [3,3,3,3,3,3,3,3,2,2,2,1]
     
     after that just iterate from strt and total = total + min(leftm[i], rightm[i]) - h[i]
     
     
  2. 2 ptr technique: tc: O(n) sc: O(1):-
        
        its same as 1st approach but we dont make array we just keep track of leftmax and right max and we iterate from left and right
        Understand in code better in code       
        
  LeetCode 42: https://leetcode.com/problems/trapping-rain-water/
  YT: https://www.youtube.com/watch?v=hI0A_UOgdD8
 """
 
 ######### Method 1 ##########
 class Solution:
    def trap(self, h: List[int]) -> int:
        s = 0
        n = len(h)
        
        left = [0]*n
        right = [0]*n
        
        left[0] = h[0]
        right[-1] = h[-1]
        
        l, r = 1, n-2
        
        while l < n and r >= 0:
            left[l] = max(left[l-1], h[l])
            right[r] = max(right[r+1], h[r])
            
            l += 1
            r -= 1
            
        for i in range(n):
            s += min(left[i], right[i]) - h[i]

        return s
        
  ########## Method 2 ##########
  
  class Solution:
    def trap(self, h: List[int]) -> int:
        s = 0
        n = len(h)
        
        l, r = 0, n-1
        leftm, rightm = h[l], h[r]
        
        while l < r:
            if leftm < rightm:
                l += 1
                leftm = max(leftm, h[l])
                s += leftm - h[l] 
            else:
                r -= 1
                rightm = max(rightm, h[r])
                s += rightm-h[r]
                
        return s
      
      
