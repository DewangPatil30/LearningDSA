"""
Approach:
      
      1. Simple MergeSort just check if left[i] <= 2*right[j]:
            if not count += len(left)-i
           return sorted(left + right)

LeetCode 493: https://leetcode.com/problems/reverse-pairs/

"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(left, right):
            
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= 2*right[j]:
                    i += 1
                else:
                    cnt[0] += len(left)-i
                    j += 1
                    
            return sorted(left + right)
            

        def sort(arr):
            if len(arr) <= 1: return arr
            mid = (len(arr)+1)//2
            
            left = sort(arr[:mid])
            right = sort(arr[mid:])
            
            return merge(left, right)
        
        cnt = [0]
        sort(nums)
        return cnt[0]
    
    
