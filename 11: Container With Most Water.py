class Solution:
    def maxArea(self, h: List[int]) -> int:
        
        res = 0

        l, r = 0, len(h)-1
        while l < r:
            
            if h[l] > h[r]:
                vol = (r-l) * h[r]
                r -= 1
            else:
                vol = (r-l) * h[l]
                l += 1
                
            if vol > res:
                res = vol
                
        return res
