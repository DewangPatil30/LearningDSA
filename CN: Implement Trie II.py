"""
Approach: Its the Enhanced Trie, Here, instead of taking "End" as boolean 
          we take it as integer so we can check how many words are ending with perticular character
          Also, we take prefix data to tell how many are starting with perticular prefix
          
       Defination: class TrieNode:
                      def __init__(self):
                          self.children = {}
                          self.prefix = 0
                          self.end = 0
                          
        1. For Inserting: take cur as self.root iterate through the string if c not in childern than add and prefix += 1 at last end += 1
        2. Maa Chudao Code se samajlo
"""
class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = 0
		self.prefix = 0

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children:
				curr.children[c] = TrieNode()
			curr = curr.children[c]
			curr.prefix += 1
		curr.end += 1
        
	def countWordsEqualTo(self, word):
		cur = self.root
		for c in word:
			if c not in cur.children: return 0
			cur = cur.children[c]
		return cur.end
    
	def countWordsStartingWith(self, word):
		cur = self.root
		for c in word:
			if c not in cur.children: return 0
			cur = cur.children[c]
		return cur.prefix
    
	def erase(self, word):
		curr = self.root
		for c in word:
			if c not in curr.children: return
			curr.prefix -= 1 
			curr = curr.children[c]
		curr.end -= 1 if curr.end != 0 else 0

