"""
2 Methods:  
    eg: strs = ["eat","tea","tan","ate","nat","bat"]

    1. sort the list strs------ nested loop for i in list for j in i 
        append list[i] first and than each list[j] in temp list if SORTED LIST[i] == EACH LIST[J]
        also maintain seen set to handle repeated.  
        
        TC = O(N^2 log N) SC = O(N)
        
    2. COUNTING EACH CHARACRTER IN EACH STR:-
          Maintain a decaultdict(list) //eg: ():[]// for st in strs for c in st: 
          count array to store the count of characters out of 26 characters in each st
          
          than this count array will become the key and st will be appended in map(count).append(st)
          
          TC = O(N^2) SC = O(N)
          
     LeetCode 49: https://leetcode.com/problems/group-anagrams/
     YT NEETCODE: https://www.youtube.com/watch?v=vzdNOK2oB2E
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()
    
        
