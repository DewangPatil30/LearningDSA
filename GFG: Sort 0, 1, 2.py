"""
Approach :-
    1. Two ptr technique: tc = O(n) sc = O(1)
     
          mid, l, r = 0, 0, n-1
          while mid <= r:
          mid = 0 then swap(mid, l) l++  mid++
          elif mid = 1 then mid ++ 
          elif mid = 2 then swap(mid, r) r--
    GFG: https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/0/#
"""

class Solution:
    def sort012(self,arr,n):
        
        l, mid, r = 0, 0, n-1
        while mid <= r:
            if arr[mid] == 0:
                arr[mid], arr[l] = arr[l], arr[mid]
                mid += 1
                l += 1
            elif arr[mid] == 1:
                mid += 1
                
            elif arr[mid] == 2:
                arr[mid], arr[r] = arr[r], arr[mid]
                r -= 1
                
        
