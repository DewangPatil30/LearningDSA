"""
[1, 5, 7, 1] 

res = k - arr[i] 
if res in m: ans += m[res]

add arr[i] in m if not present else m[arr[i]] += 1
"""


class Solution:
    def getPairsCount(self, arr, n, k):
          
        m = dict()
        ans = 0
        for i in range(n):
            res = k - arr[i]
            if res in m:
                ans += m[res]
                
            if arr[i] not in m:
                m[arr[i]] = 0
            
            m[arr[i]] += 1
                    
        return ans
      
      
