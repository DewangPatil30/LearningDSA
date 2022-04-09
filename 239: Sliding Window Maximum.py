"""
Approaches:
    
    1. Check for every window the maximum and store: TC: O(N*K) SC: O(1)
    2. Using Deque: TC: O(N) + O(K) SC: O(N)
        
        a. Take a Deque, while r < len(nums)
        b. while deque and deque[-1].val < nums[i]: pop from back
        c. Than append index to left
        d. If l > deque[0]: deque.popleft()
        e. if r+1 >= k:
            res.append(nums[deque.front()])
            l += 1
         r += 1
    
    LeetCode 239: https://leetcode.com/problems/sliding-window-maximum/
    YT NeetCode: https://www.youtube.com/watch?v=DfljaUwZsOk
"""
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        dq = collections.deque()
        
        l = r = 0
        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            
            if l > dq[0]:
                dq.popleft()
                
            if k <= r+1:
                res.append(nums[dq[0]])
                l += 1
            
            r += 1
        
        return res
                
                
