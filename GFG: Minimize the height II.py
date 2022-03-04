"""
1. sort the array
2. minimum diff is arr[n-1] - arr[0] ie, res = this
3. small, large = arr[0]+k, arr[n-1]-k

BADE SE K - KRO , CHOTE M K + KRO

4. for i in range(n-1):
      mi = min(small, arr[i+1]-k)
      mx = max(large, arr[i]+k)
      
5. mi < 0: continue
6. res = min(res, mx-mi)

GFG: https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#
YT: https://www.youtube.com/watch?v=Av7vSnPSCtw
"""



class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        
        arr.sort()
        res = arr[-1] - arr[0]
        
        s, l = arr[0]+k, arr[-1] - k
        for i in range(n-1):
            
            mi = min(s, arr[i+1]-k)
            ma = max(l, arr[i]+k)
            
            if mi < 0:
                continue
            
            res = min(res, ma-mi)
            
        return res
      
      
