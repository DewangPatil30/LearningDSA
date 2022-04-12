"""
   Approaches: 
            
            1. Brute Force: sort the array  O(n log n)
            2. using MaxHeap:   O(N) for heapify + O(k log n) for removing elements k times
                                ie, O(N) + O(KlogN)
    
    LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)): nums[i] = -nums[i]
        heapify(nums)
        for i in range(k-1): heappop(nums)
        
        return -nums[0]
            
        
