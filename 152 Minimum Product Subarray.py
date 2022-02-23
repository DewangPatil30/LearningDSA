class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxp = max(nums)
        currmin, currmax = 1, 1
        
        for n in nums:
            if n == 0:
                currmin, currmax = 1, 1
                continue
            
            temp = currmax * n
            currmax = max(currmax * n, currmin * n, n)
            currmin = min(temp, currmin * n, n)
            
            maxp = max(currmin, currmax, maxp)
            
        return maxp
