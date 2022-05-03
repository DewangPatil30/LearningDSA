"""
    
    Approaches: 
            
            1. Sort The Array:  O(N log N) O(N)
                a. clone the array than sort the cloned arr
                b. check for first and last non eq element for Ith index
                return r-l+1 if r-l > 0 else 0
                
            2. Using Stack: O(N)  O(N) for stack:
                we need to check the correct position of smallest unsorted element and lasrgest unsorted element
                to do this we store the index of each element in stack if its increasing if not than pop index and
                store in left_bound as min(left_bound, ind) 
                
                simi, for largest, parse arr in reverse and store in right_bound as max(right_bound, ind)
            return r-l+1 if r-l > 0 else 0    
            
LeetCode 581: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""

################# SORTING ARRAY #################

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        nums2.sort()

        l, r = 0, 0
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                l = i
                break
        else: return 0    
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != nums2[i]:
                r = i
                break

        return r-l+1
      
################# Using Stack ##############

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if not nums or len(nums) == 1: return 0
        
        st = [] 
        l, r = len(nums), 0
        
        for i in range(len(nums)):
            while st and nums[st[-1]] > nums[i]:
                l = min(l, st.pop())
                
            st.append(i)

        for i in range(len(nums)-1, -1, -1):
            while st and nums[st[-1]] < nums[i]:
                r = max(r, st.pop())
                
            st.append(i)

        return r-l+1 if r - l > 0 else 0
    
  
