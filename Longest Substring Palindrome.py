class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        long = ''
        l = 0
        
        strt = end = 0
        
        for i in range(len(s)-1):
        
            //FOR EVEN
            
            low = i
            high = i+1
                            
            while low >= 0 and high < len(s) and s[low] == s[high]:
                
                if high - low + 1 > l:
                    l = high-low+1
                    strt = low
                    end = high
                    
                low -= 1
                high += 1
                    
            low = i
            high = i+2
            
            //FOR ODD
            while low >= 0 and high < len(s) and s[low] == s[high]:
                
                if high - low + 1 > l:
                    l = high-low+1
                    strt = low
                    end = high
                    
                low -= 1
                high += 1
                
        return s[strt:end+1]
        
