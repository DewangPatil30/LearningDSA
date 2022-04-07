"""
Approach:
    
    a. Insert all the strings in the Trie
    b. Take max_str = ""
    c. Check all the string if all end == True than 
       if len s > len max_str or (len s == len max_str and s < max_str): max_str = s
       else: continue
    return max_str if not "" else None

CN: https://www.codingninjas.com/codestudio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0
YT: https://www.youtube.com/watch?v=AWnBa91lThI
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def isPrefix(word, root) -> bool:
	cur = root
	for c in word:
		if c in cur.children: 
			cur = cur.children[c]
			if not cur.end: return False
		else: return False
        
	return True

def completeString(n: int, arr: List[str])-> str:
	root = TrieNode()
	cur = root
    
	for s in arr:
		for c in s:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		cur.end = True
		cur = root
    
    
	mxs = ""
	cur = root
	for s in arr:
		if isPrefix(s, root):
			if len(s) > len(mxs) or (len(s) == len(mxs) and s < mxs):
				mxs = s
                
	return mxs if mxs else None
                
            
