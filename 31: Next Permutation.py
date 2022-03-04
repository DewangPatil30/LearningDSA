# Approach :-

#   Check from the end of the array till its increasing, when the left element is small than the right, Its the pivot point
#   Check the first greater element than the pivot element ie, strt again from last of array and check till pivot until we got the smallest element which is larger than pivot
#   Swap the next larger and pivot than than sort the array after the pivot.
#   If first step is failed, ie, the array is sorted in decending oreder so just sort the array.
#   If you like it please upvote this post
  
# TC: O(NlogN), SC: O(1)

# Code Below:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n == 1: return 
        elif n == 2: 
            nums[0], nums[1] = nums[1], nums[0]
            return 
        
        found = False
        p = 0
        for r in range(n-1, 0, -1):
            if nums[r-1] < nums[r]:
                p = r-1
                found = True
                break
            
        if not found: 
            nums.sort()
            return 
        
        for r in range(n-1, 0, -1):
            if nums[r] > nums[p]:
                nums[r], nums[p] = nums[p], nums[r]
                break
            
        nums[p+1:] = list(sorted(nums[p+1:]))
