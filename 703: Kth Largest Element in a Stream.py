"""
Approach: Using Heap: Time complexity: O(N.log(N) + M.log(k)) = O(N⋅log(N)+M⋅log(k))
    
    A. In the constructor, create a min heap using the elements from nums. Then, pop from the heap until heap.length == k.
    B. For every call to add():

        a. First, push val into heap.
        b. Next, check if heap.length > k. If so, pop from the heap.
        c. Finally, return the smallest value from the heap, which we can get in O(1) O(1) time.
        
    LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        heapify(nums)
        self.heap = nums
        self.k = k
        
        n = len(self.heap)
        while n > k:
            heappop(self.heap)
            n -= 1
            
    def add(self, val: int) -> int:
        
        heappush(self.heap, val)
        if len(self.heap) > self.k: heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
