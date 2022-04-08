"""
Approaches: 
    
    1. Using nested loops: TC:O(N^2)
    2. Using Trie: TC:O(N) + O(M):
            
            a. Insert all the element bitwise into a trie:
                First see max len of bit string in the array so upto that length 
                we will take no of bits to store in trie
            b. tarvasal through all the elements in array:
                for each ele take bit string to max len 
            c. Travasal through bit string and check if the opposite bit is available 
                if available than take that else take same bit
            Do this for all bits and store max XOR than return
            
      LeetCode 421: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
      YT: https://www.youtube.com/watch?v=EIhAwfHubE8
"""

class TrieNode:
    def __init__(self):
        self.bits = [None]*2
        
        
class Trie:
    def __init__(self, ln):
        self.root = TrieNode()
        self.ln = ln
        
    def getBinary(self, n):
        b = "{:032b}".format(n)
        diff = len(b) - self.ln
        s = b[diff:]
        return s

    def insert(self, n):
        binary = self.getBinary(n)
        cur = self.root
        
        for i in binary:
            bit = int(i)
            if not cur.bits[bit]:
                cur.bits[bit] = TrieNode()
            cur = cur.bits[bit]
            
    def getMax(self, arr):
        
        maxnum = 0
        for a in arr:
            num = ''
            binary = self.getBinary(a)
            cur = self.root

            for i in binary:
                bit = int(i)
                if cur.bits[1-bit]:
                    num += str(1-bit)
                    cur = cur.bits[1-bit]
                else:
                    num += str(bit)
                    cur = cur.bits[bit]
                        
            maxnum = max(maxnum, int(num, 2) ^ a)
            
        return maxnum
    

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        max_len = len(bin(max(nums)))-2  #Max len of binary string
        trie = Trie(max_len)
        
        for i in nums:
            trie.insert(i)
            
        return trie.getMax(nums)
