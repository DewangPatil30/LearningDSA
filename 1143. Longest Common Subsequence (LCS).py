"""
Approaches:

    1. Recursion: TC: O(2^N) Top Down
        
        a. Run LCS fn with strt indexes i, j
        b. If i == len(s1) or j == len(s2): return 0
        c. if s1[i] == s2[j]: return 1 + LCS(i+1, j+1)
        d. else return max( LCS(i+1, j), LCS(i, j+1) )
        
     2. Dynamic Programming :- TC: O(NM) SC: O(NM) Buttom Up 
     
        a. create table LCS of n+1 * m+1 size with 0th row and column set to 0 and all -1
        2. for i in range(n) for j in range(m) 
            if s1[i] == s2[j]: 
                LCS[i+1][j+1] = 1 + LCS[i][j]
            else: LCS[i+1][j+1] = max( LCS[i][j+1], LCS[i+1][j] )
            return lcs[-1][-1]
            
      
   LeetCode 1143: https://leetcode.com/problems/longest-common-subsequence/
   YT Abdul Bari: https://www.youtube.com/watch?v=sSno9rV8Rhg
"""

class Solution:
    def longestCommonSubsequence(self, st1: str, st2: str) -> int:
        
        n = len(st1)
        m = len(st2)
        
        lcs = []
        
        for i in range(n+1):
            temp = []
            for j in range(m+1):
                if i == 0 or j == 0:
                    temp.append(0)
                else: temp.append(-1)
            lcs.append(temp)
            
        
        for i in range(n):
            for j in range(m):
                
                if st1[i] == st2[j]:
                    lcs[i+1][j+1] = 1 + lcs[i][j]
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
                    
        return lcs[-1][-1]
    
    
