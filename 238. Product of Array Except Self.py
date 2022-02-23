class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1]*n
        
        for i in range(n): #for prefix
            if i != 0:
                res[i] = res[i-1] * nums[i-1]
        
        post = nums[n-1] #for postfix

        for i in range(n-1, 0, -1):
            res[i-1] = res[i-1] * post
            post *= nums[i-1]
            
        return res
