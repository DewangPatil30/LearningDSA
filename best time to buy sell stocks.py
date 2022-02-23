class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        maxp = -1
        l, r = 0, 1
        
        while r < len(p):
            
            if p[l] > p[r]:
                l = r
            else:
                locprof = p[r] - p[l]
                
                if locprof > maxp:
                    maxp = locprof
                
            r += 1
            
        if maxp < 1:
            return 0
        return maxp
