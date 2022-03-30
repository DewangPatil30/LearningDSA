"""
Approaches: 
  eg arr: {15,-2,2,-8,1,7,10,23}

    1. Brute Force: TC: O(N^3): 
         N^2 for subarrays creation * N for sum of each subarray.
         
    2. Kardane's Algo: TC: O(n) SC: O(n):
         a. Take a hashmap to store prefix sum with its index eg: [15: 0, 13: 1, 7: 3 ---]
         b. Check if s == 0: maxl = max(maxl, i+1) else:
         c. if s in m than maxl = max(maxl, i - m[s])
         d. else m[s] = i
         Return maxl
         
    GFG: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#
    YT: https://www.youtube.com/watch?v=xmguZ6GbatA
"""
class Solution:
    def maxLen(self, n, arr):

        m = {}
        s = 0
        maxl = 0
        for i in range(n):
            s += arr[i]
            if s == 0: 
                maxl = max(maxl, i+1)
            elif s in m:
                maxl = max(maxl, (i - (m[s])))
            else:
                m[s] = i
            
        return maxl
      
      
