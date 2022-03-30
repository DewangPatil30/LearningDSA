"""
  3 Approaches:
      1. Recursive: TC: O(2^n)
      2. DP: Buttom up : TC: O(n) SC: O(n):
            a. Initialize dp array NxM by 1 (Precisely last row and last column must be 1) bcoz for last row and last column [Down + Right] == 1
            b. than each dp[i][j] = dp[i][j+1] + dp[i+1][j] for n-2 -> 0 and m-2 -> 0
            c. return dp[0][0]
      3. Mathematical: (m*n)! / (m!*n!)
      
LeetCode 62: https://leetcode.com/problems/unique-paths/
YT NeetCode: https://www.youtube.com/watch?v=IlEsdxuD4lY
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1]*m]*n
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
                
        return dp[0][0]
      
