"""
Approaches: 
        
        1. Using Sorted array: TC:O(N) for add SC:O(N) for stack
             
             a. while adding val in stream check if stream[-1] > val
             b. while stream[-1] > val: tempStack.push(stream.pop())
             c. while tempStack: stream.push(tempstack.pop())
             d. Return mid if odd else mid + mid+1 / 2
             
        2. Using 2 Heaps: MinHeap and MaxHeap
                TC: O(log n) for add   SC: O(N)
             
             a. take small as maxheap and large as min heap
             b. while add check if small and large and small[0] > large[0]
             c. If yes: pop small and push in large
             
             d. check if len(small) > len(large) + 1  and vice versa        ie, diff is size is 2 or greater coz 1 diff is allowed
                if true pop from greater size and push in smaller size
                
             e. For median fn: if len small > large: return small[0] if opposit than large[0]
                else: return small[0] + large[0] / 2

LeetCode 295: https://leetcode.com/problems/find-median-from-data-stream/
YT: https://www.youtube.com/watch?v=itmhHWaHupI
"""

from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = heappop(self.small)
            heappush(self.large, -val)
            
        if len(self.small) > len(self.large) + 1:
            val = heappop(self.small)
            heappush(self.large, -val)    
        
        elif len(self.small) + 1 < len(self.large):
            val = heappop(self.large)
            heappush(self.small, -val) 
        
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large): return -self.small[0]
        if len(self.small) < len(self.large): return self.large[0]
        return (-self.small[0] + self.large[0]) / 2

