"""
Approach:

        1. Sliding window: O(N) and O(t):
               
               We will use 2 pointer method here, we start l, r from 0, we also maintain 2 count hashmaps window and countT for counting chars in t and our window.

                Now, we start iterating from char at r, If c (ie, c = s[r]) is in countT than we increment the count of c in our window, 
                Our target is to get window[c] >= countT[c] for every char in t.

                To check the above condition Effeciently we use 2 variables have and need where need is len of countT, 
                and we incerment have when window[c] >= countT[c] (ie, when we have more no of req chars in our window than we need).

                So, when we reach c = "C" for index = 5, we have our have == need now we store left and right index to res if resLen is greater than curr len, 
                Than, we need to remove chars from our left coz end goal is to get minimum str, so we loop till have == need, we check if cl (ie, cl = s[l]) is in countT 
                if yes than we decrement count of cl from window. 

                now we check if window[cl] < countT[cl] if yes than we decrement have, Finally we shift l to l+1 ie l += 1
                In the end we return s[res[0], res[1]+1] if resLen != inf else "".

LeetCode 76: https://leetcode.com/problems/minimum-window-substring/
NeetCode: https://www.youtube.com/watch?v=jSto0O4AJbM
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t: return ""  # edge case
		
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)       #Count chars in t
            
		l = 0
        have, need = 0, len(countT)     
        res, resLen = [-1, -1], inf
        
        for r in range(len(s)):
            c = s[r]
            if c in countT:
                window[c] = 1 + window.get(c, 0)      # if c is in countT than inc the value in window 
                
            if c in countT and window[c] == countT[c]:
                have += 1     # if any char is satisfied than inc have
            
            while have == need:
                cl = s[l]
                
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1 #storing res coz we found our substr
                
                if cl in countT:
                    window[cl] = window.get(cl, 1) - 1    ''' dec count if left char is in countT else skip'''
                
                if cl in countT and window[cl] < countT[cl]:
                    have -= 1   #dec have id cl is less than required in window
                        
                l += 1
                
                
        return s[res[0]: res[1]+1] if resLen != inf else ""
                    
