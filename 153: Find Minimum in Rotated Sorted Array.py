class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        mini = nums[0]
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            if nums[l] < nums[r]:
                if mini > nums[l]:
                    mini = nums[l]
                break
                
            mid = (l + r) // 2
            
            if mini > nums[mid]:
                mini = nums[mid]
                
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        return mini
