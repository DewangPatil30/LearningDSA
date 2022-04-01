"""
Approach: eg arrival: [0900 0940 0950 1100 1500 1800]
             departure: [0910 1200 1120 1130 1900 2000]
        
        a. sort both arrival and dep array
        b. plat = 1 and j = 0 {For travasing in dep array}
        c. loop from 1 to n 
        d. If dep[j] >= arrival[i] {where 1 <= i < n} plat += 1 else j += 1
        
        return plat
        TC: O(NlogN) SC:O(1)
        
    GFG: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
    YT: https://www.youtube.com/watch?v=dxVcMDI7vyI
"""
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        
        plat = 1
        j = 0
        for i in range(1, n):
            if arr[i] <= dep[j]:
                plat += 1
            else:
                j += 1
        return plat
      
      
