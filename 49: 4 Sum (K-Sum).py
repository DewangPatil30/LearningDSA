"""
In order to solve this problem you need to do parent problems :
      1. Two Sum II
      2. 3 Sum

If you get these 2 problems this problem will be piece of cake. all ksum problem can be divided into above two problems

Approach and Intution :
      SORT THE ARRAY
      1. Reduce K sum problem to K – 1 sum Problem
      2. When k == 2, than its Two Sum II problem

But we need to sort the array first, Therefore, We could use recursion to solve this problem. Time complexity will be O(n^(k-1)).

LeetCode 49: https://leetcode.com/problems/4sum/
YT NeetCode: https://www.youtube.com/watch?v=EYeR-_1NRlQ
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def ksum(k, strt, target):
            if k != 2:
                for i in range(strt, len(nums) - k + 1): #must leave k+1 vals to set in quad
                    if i > strt and nums[i] == nums[i-1]: # avoid duplicates
                        continue 
                    
                    quad.append(nums[i])
                    ksum(k-1, i + 1, target - nums[i])
                    quad.pop()
                return 
            
            l, r = strt, len(nums)-1    # Base Case 2 sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                        
        nums.sort()         
        res, quad = [], []
        ksum(4, 0, target)
        return res
      
      
