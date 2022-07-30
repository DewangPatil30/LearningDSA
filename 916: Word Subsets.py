"""
Approach:

        EG: ["amazon","apple","facebook","google","leetcode"]
            ["lo","eo"]
        
        1. Need & Have Method: O(nk)  O(Kmax)
            a. first create map need using, take temp map and create need
                so need map look like: need = {l:1, e:1, o:1} where {c: max(c) in every str}
            
            b. Now, for every word in A we create the have map and take h, n represent have num and need num
                if have[c] == need[c] we increment h += 1 and mark c in ignore so we dont increment for it again (JUST TO MAKE IT FASTER)
            c. Finally if h == n: res.append(word)
            
LeetCode 916: https://leetcode.com/problems/word-subsets/
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        
        need = {}
        for w in words2:
            temp = {}
            
            for c in w:
                temp[c] = 1 + temp.get(c, 0)
            
            if not need: 
                need = temp
            else:
                for k in temp:
                    need[k] = max(need[k], temp[k]) if k in need else temp[k]
        
        
        n, h = len(need), 0
        for w in words1:
            have = {}
            ignore = set()
            h = 0
            
            for c in w:
                if c in need:
                    have[c] = 1 + have.get(c, 0)
                    
                if c in need and have[c] == need[c] and c not in ignore:
                    h += 1
                    ignore.add(c)
                    
            if h == n:
                res.append(w)
                
        return res
                    
                
    
