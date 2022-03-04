"""
Floyds Entry point of a cycle: https://leetcode.com/problems/find-the-duplicate-number/solution/
LeetCode 287: https://leetcode.com/problems/find-the-duplicate-number/
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
            
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
      
      
