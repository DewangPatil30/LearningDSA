class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return 
        elif len(nums) == 3 and sum(nums) == 0:
            return [nums]
        
        nums.sort()
        res = []
        
        for i, v in enumerate(nums):        
            if i > 0 and v == nums[i-1]:   #if val already used in first position than skip 
                continue
                
            l = i+1              #[-3,-3,0,1,2] so strt l will strt frm i+1
            r = len(nums)-1      #there should be val left for c in tsum = a+b+c
            
            while l < r:
                tsum = v + nums[l] + nums[r]
                
                if tsum > 0:     #if sum > 0 then make it small by shifting right
                    r -= 1
                elif tsum < 0:   #if sum < 0 then make it big by shifting left
                    l += 1
                    
                else:
                    res.append([v,nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return res
            
