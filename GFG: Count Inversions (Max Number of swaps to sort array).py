"""
2 Methods:
  1. N^2 solution: two nested loops i -> n-1, j = i+1 -> n: 
                   if arr[i] > arr[j]: count += 1
                   
  2. Merge Sort: N log N Solution (DIVIDE AND CONCOUR): 
  
      apply merge sort and if arr[i] > arr[j]: add count += mid-i+1 in condition   
      
  GFG: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#
  Solution: https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#
"""

class Solution:
  def inversionCount(self, arr, n):
        
        def merge(arr, left, mid, right):
            i, j, k = left, mid+1, left   
            count = 0
        
            while i <= mid and j <= right:
        
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    count += (mid-i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
                
            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1
                
            return count

        def mergeSort(arr, left, right):
            count = 0
            if left < right:
                mid = (left + right)//2
        
                count += mergeSort(arr, left, mid)
                count += mergeSort(arr, mid+1, right)
        
                count += merge(arr, left, mid, right)
                
            return count
            
            
        temp = [0]*n
        return mergeSort(arr, 0, n-1)
      
      
      
