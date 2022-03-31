"""
Approaches 2:   Eg arr = [100,4,200,1,3,2]

    1. By Sorting Array: TC:O(n log n) SC: O(1)
          Sort the array for each i if i+1 exists than l += 1 else l = 1
          
    2. By Drwaing number line: eg: TC:O(N) SC: O(N) [1,2,3,4,....100......200]:
          
          for any strt of the sequence there is no strt-1 in array so its the strt of seq
          a. Make set of array:
          b. for each ele in array if ele-1 not in set: strt = element
          c. while strt+1 in set l += 1 else l = 1 and break
          return max len
          
     LeetCode 128: https://leetcode.com/problems/longest-consecutive-sequence/
     YT NeetCode: https://www.youtube.com/watch?v=P6RZZMu_maU
"""
class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        s = set(arr)
        maxl = l = 1
        n = len(arr)
        if n < 2: return n

        for i in list(s):   # Taking list(s) so no duplicate remains (REDUCES RUNTIME MS)
            if i-1 not in s:
                strt = i
                while strt+1 in s:
                    l += 1
                    strt += 1
                    maxl = max(maxl, l)
            l = 1        

        return maxl
        
