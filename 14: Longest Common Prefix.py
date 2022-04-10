"""
Approaches:
    
    1. Brute Force (VERTICAL SCANNING): TC: O(N * minlen)   SC: O(1):
        
        a. Take the minimum length of str in strs 
        b. for prefix_ind in range(minlen)
        c. if all strs[i][prefix_ind] == strs[i+1][prefix_ind] for i in range(len(srs)-1)
            prefix += strs[0][prefix_ind]
        d. Else return prefix 
        
    2. Using Trie: TC: O(N*M)
        
        a. Create Trie with childern and count for counting occourances of characters
        b. Insert all char of all strs in trie and count += 1
        c. Iterate through the trie and check len of children == 1 and count == len(strs)
            than add in prefix 
         Else return prefix
         
     LeetCode 14: https://leetcode.com/problems/longest-common-prefix/
"""
class TrieNode:
    def __init__(self, count = 0):
        self.children = {}
        self.count = count
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, st):
        cur = self.root
        
        for c in st:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur.count += 1
            cur = cur.children[c]
            
            
    def longestPrefix(self, minlen):
        cur = self.root
        pre = ''
        
        while len(cur.children) == 1 and cur.count == minlen:
            for c in cur.children:
                pre += c
            cur = cur.children[c]
            
        return pre

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]
        
        trie = Trie()
        for st in strs:
            if not st: return ""
            trie.insert(st)
        
        return trie.longestPrefix(len(strs))
        
        
        
        
        ########### Brute Force Vertical Scanning ##############
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        minlen = 200
        for st in strs:
            minlen = min(minlen, len(st))

        lprefix = ''
        for pre in range(minlen):
            if all(strs[i][pre] == strs[i+1][pre] for i in range(len(strs)-1)):
                lprefix += strs[0][pre]
            else: return lprefix

        return lprefix
