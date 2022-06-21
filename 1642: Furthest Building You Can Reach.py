"""
Approach:  
        1. Using MinHeap:
            
            a. Take diff ie, H[i+1] - H[i] if diff > 0 than push in heap
            b. if len of heap is <= ladders than ladders can handle all previous heights 
            c. if len of heap excedes ladders than we need to use bricks so we will use brick on the minimum diff
                so bricks -= heappop(heap)
            d. if bricks < 0 than return i
            return n-1
            
   LeetCode 1642: https://leetcode.com/problems/furthest-building-you-can-reach/
   YT: https://www.youtube.com/watch?v=7LmgzOCnZQk
"""

class Solution:
    def furthestBuilding(self, nums: List[int], bricks: int, ladders: int) -> int:
        
        n = len(nums)
        lused = []
        for i in range(n-1):
                
            diff = nums[i+1] - nums[i]
            if diff > 0: heappush(lused, diff)
            
            if len(lused) > ladders: bricks -= heappop(lused)
            if bricks < 0: return i
                
        
        return n-1
    
    
