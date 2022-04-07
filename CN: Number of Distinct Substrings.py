"""
Approaches:
        
        1. Use set and make substrings: TC:O(N^2 log M) SC:O(N^3) coz we storing each distinct substr in set
        2. Use Trie: TC:O(N^2) SC: 26 * 26 .... unexplainable:
                
               a. Create Trie with only self.children
               b. while inserting increment count if char not in children and return count
               c. In outer execution for all substrs count += insert(words[i:])
               return count
        
        CN: https://www.codingninjas.com/codestudio/problems/number-of-distinct-substring_1465938?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
        YT: https://www.youtube.com/watch?v=RV0QeTyHZxo
"""

class TrieNode:
	def __init__(self):
		self.children = {}

class Trie:
	def __init__(self):
		self.root = TrieNode()
        
	def insertcountDistinct(self, word):
		cur = self.root
		cnt = 0
		for c in word:
			if c not in cur.children:
				cnt += 1
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		return cnt
        
        
def distinctSubstring(word):
	trie = Trie()
	cnt = 0
	for i in range(len(word)):
		cnt += trie.insertcountDistinct(word[i:])
	return cnt
