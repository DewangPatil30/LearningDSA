"""
Approach:
        
        1. Merge 2 sorted array formula:
                    Understand with code

GFG: https://practice.geeksforgeeks.org/problems/max-sum-path-in-two-arrays/0/?track=amazon-arrays&batchId=192#
"""

class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        
        i, j = 0, 0
        sum1, sum2, res = 0, 0, 0 
        
        
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
                
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
                
            else:
                res += max(sum1, sum2) + arr1[i]
                sum1, sum2 = 0, 0
                
                i += 1; j += 1
                
        while i < m:
            sum1 += arr1[i]
            i += 1
            
        while j < n:
            sum2 += arr2[j]
            j += 1
        
        res += max(sum1, sum2)
        return res
        
        
