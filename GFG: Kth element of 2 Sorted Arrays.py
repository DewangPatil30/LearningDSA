"""
Approaches: 
    1. Merge 2 sorted arrays than take kth element: TC:O(n+m) SC:O(N+M)
    2. Using Merge algo take the Kth element out: TC:O(K) SC:O(1)
    3. Binary Search By taking k left elements: TC:O(log min(n,m)) SC:O(1):
        
        Intution: K left elements from 2 sorted elements will be smaller than all the elements remaining on the right.
                  So just take out max(l1, l2) ie, max of leftmost element of first array and second array
                  Now the challenge is how to select how many of k elements should we take from 1st sorted and rest from 2nd sorted
                  so for that condition is l1 <= r2 and l2 <= r1
                  
        Algo: we will always consider smaller array to be the first array
              a. Take low and high is low = max(0, k-m), min(k, n)
              run binary search:
              b. cut1 = (low + high) >> 1 ie, //2
                 cut2 = k-cut1
                   
              c. l1, l2 = arr1[cut1-1], arr2[cut2-1]  IF CUT1 != 0 AND CUT2 != 0 else INT_MIN
              d. r1, r2 = arr1[cut1], arr2[cut2]  IF CUT1 != n AND CUT2 != m else INT_MAX

              e. if (l1 <= r2 and l2 <= r1):
                  return max(l1, l2)
                if l1 > r2: r = cut1-1
                else l = cut1+1

YT: https://www.youtube.com/watch?v=nv7F4PiLUzo
GFG: https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1#
"""

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m: return self.kthElement(arr2, arr1, m, n, k)
        
        l = max(0, k-m)
        r = min(k, n)
        
        while l <= r:
            cut1 = (l+r) >> 1
            cut2 = k - cut1
            
            l1 = -99999999 if cut1 == 0 else arr1[cut1-1]
            l2 = -99999999 if cut2 == 0 else arr2[cut2-1]
            
            r1 = 99999999 if cut1 == n else arr1[cut1]
            r2 = 99999999 if cut2 == m else arr2[cut2]
        
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                r = cut1-1
            else:
                l = cut1+1
                
        return 1
      
      
