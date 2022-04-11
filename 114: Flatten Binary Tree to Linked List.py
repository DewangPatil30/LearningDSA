"""
  Approach: 
        
        a. Goto right most first, store each right for backtracking
        b. root.right = rt[0]
           root.lelt = None
           rt[0] = root   # stored last rightmost value 
        c. b step is done when
            flat(root.right)
            flat(root.left) is completed
            
  LeetCode 114: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def flat(root):
            if not root: return
            
            
            flat(root.right)
            flat(root.left)
            
            root.right = rt[0]
            root.left = None
            rt[0] = root
                
            return root
        
        rt = [None]
        return flat(root)
    
    
 # Another Right Solution:

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        if not root: return
        
        s = [root]
        pre = []
        
        while s:
            temp = s.pop()
            pre.append(temp)
            if temp.right: s.append(temp.right)
            if temp.left: s.append(temp.left)
        
        pre.pop(0)
        while pre:
            root.left = None
            root.right = pre.pop(0)
            root = root.right
                
