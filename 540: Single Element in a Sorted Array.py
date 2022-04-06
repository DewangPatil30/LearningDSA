"""
Approaches:
    
    1. Neive approach: TC: O(N):-
        1a. travase through the array by checking next element return ele if not eq to next
        1b. return XOR of all elements in array (Bcoz XOR of ele with itself is 0)
    
    2. Binary Search: TC:O(log N):-
        a. Take l = 0 and r from last 2nd ele, ie, r = len(arr)-2
        b. Run the binary search l <= r
        c. Check if mid is odd or even if odd check mid-1 ie, previous even ele is same or not 
            if same than l = mid + 1 else r = mid - 1, this same opposit in case of even
            OR JUST CHECK IF ARR[MID] == ARR[MID^1] COZ ODD XOR 1 GIVES PREVIOUS EVEN AND VISE VERSA
        return arr[l]
        
     LeetCode 540: https://leetcode.com/problems/single-element-in-a-sorted-array/
     YT: https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-2
        while l <= r:
            mid = (l+r) >> 1 # same as //2
            if nums[mid] == nums[mid^1]:
                l += 1
            else:
                r -= 1
        
        return nums[l]
                
