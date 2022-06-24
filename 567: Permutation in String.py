"""
Approaches:

        1. Using Sliding window and sort: (N^2 log N)
        2. Using Sliding Window and Array Hashmaps: O(N) O(1):
        
           a. We take 2 Static sized array hashmaps h1 to store character and occourance of s1 chars, Simi, h2 for s2.
           b. We iterate over s2 and increment character's (Represented by ASCII Code as Array Hashmap Index) occourance
           c. If i becomes greater than n than we remove the occourance of (i-n)th characters occourance from h2
           d. Finally on each iteration we always check if h1 == h2 if so that instantly return True else if loop ends than return False.
            
           Time & Space Complexity: O(N) O(1)

LeetCode 567: https://leetcode.com/problems/permutation-in-string/
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        h2 = [0]*26
        h1 = [0]*26
        
        for c in s1: 
            h1[ord(c) - ord('a')] += 1
        
        for i in range(len(s2)):
            if i < n:
                h2[ord(s2[i]) - ord('a')] += 1
            else:
                h2[ord(s2[i]) - ord('a')] += 1
                h2[ord(s2[i-n]) - ord('a')] -= 1
                
            if h1 == h2: return True
            
        return False
            
            
