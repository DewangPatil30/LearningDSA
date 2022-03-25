"""
NOT UNDERSTOOD COMPLETELY ONLY UNDERSTOOD CODE: DP PROBLEM

GFG: https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1#
YT: https://www.youtube.com/watch?v=UQiZmkVwARg
"""

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
	    n = len(s)
	    dp = [[0 for i in range(n+1)]for i in range(n+1)]
		
	    for i in range(n+1):
	        for j in range(n+1):
		        
		        if i == 0 or j == 0: 
		            dp[i][j] = 0
		            
		        elif s[i-1] == s[j-1] and i != j: 
		            dp[i][j] = dp[i-1][j-1] + 1
		            
		        else: 
		            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
		        
        return dp[n][n]
      
      
