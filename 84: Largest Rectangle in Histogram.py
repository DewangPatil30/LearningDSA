"""
Approach: 
    
    1. Using Stack: TC:O(N) SC:O(2N):
        
        a. Take stack st to store pair of index and height, also take max height var
        b. Iterate through the array, Store the strt index i each time 
        c. Check if top value is smaller than current val, If it is than 
            pop out top value and index than check max(largest, topHeight * (i-topIndex))
        d. Set strt = topIndex
        Now there are some elements left in stack
        e. iterate through stack:
            largest = max(largest, height * (len(heights)-index)
        Return largest
        
    LeetCode 84: https://leetcode.com/problems/largest-rectangle-in-histogram/
    YT NeetCode: https://www.youtube.com/watch?v=zx5Sw9130L0
"""

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        
        largest = 0
        st = []
        
        for i, v in enumerate(h):
            strt = i
            while st and st[-1][1] > v:
                ind, height = st.pop()
                largest = max(largest, height * (i - ind))
                strt = ind
                
            st.append((strt, v))
            
        for i, v in st:
            largest = max(largest, v * (len(h)-i))
            
        return largest
                
