"""
Approach:

      1. Flatten the matrix and sort: TC: O(N*M log N*M), SC: O(N)
      2. Using Binary Search: TC: O(32 N log M) SC: O(1):
            
            a. Take low as eq to lower bound of constraint, Simi, with high
            b. Run the binary search low <= high 
            c. Now, Take mid and count how many elements in matrix are smaller eq to mid
                This will also be done by binary search in another function CountEle
            d. If count <= n//2 than low = mid + 1
                else: high = mid - 1
            Return l
            
        GFG: https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1/#
        YT: https://www.youtube.com/watch?v=63fPPOdIr2c
"""
class Solution:
    def countEle(self,arr, n, m):
        
        l = 0
        r = len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] <= m:
                l = mid+1
            else:
                r = mid-1
        return l        
    
    def median(self, matrix, r, c):

    	l = 1
    	h = 2000
    	n = r*c
    	
    	while l <= h:
    	    mid = (l+h)//2
    	    cnt = 0
    	    for arr in matrix:
    	        cnt += self.countEle(arr, n, mid)
    	
    	    if cnt <= n//2:
    	        l =  mid + 1
    	    else:
    	        h = mid-1
    	        
    	return l
