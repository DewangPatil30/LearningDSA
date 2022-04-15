"""
  Approaches:
            
            1. Linear Search: O(M*N)   O(1)
            2. Binary Search: O(Log mn)   O(1)
                intuition: 
                    As it is clearly mentioned that the given matrix will be row-wise and column-wise sorted, 
                    we can see that the elements in the matrix will be in a monotonically increasing order. 
                    So we can apply binary search to search the matrix. 
                    Consider the 2D matrix as a 1D matrix having indices from 0 to (m*n)-1 and apply binary search.
                    
  LeetCode 74: https://leetcode.com/problems/search-a-2d-matrix/
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m*n)-1
        
        while l <= r:
            mid = (l+r) >> 1
            midval = matrix[mid//n][mid%n]
            
            if midval == target: return True
            elif midval < target: l = mid+1
            else: r = mid-1
                
        return False
                
        
