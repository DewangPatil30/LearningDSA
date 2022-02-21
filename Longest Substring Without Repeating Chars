class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxl = 0
        length = 0
        m = dict()
        
        l, r = 0, 0
        
        while r < len(s):
            if s[r] not in m or l > m[s[r]]:
                m[s[r]] = r
                length = (r-l)+1 
                
            else:
                length = 0
                l = m[s[r]] + 1
                m[s[r]] = r
            
            r += 1
            
            if length > maxl:
                maxl = length
                
        return maxl
            
