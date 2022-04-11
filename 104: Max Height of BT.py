"""
Approach:
        
        1. post order trav: if not root return 0
            l = fn(root.left)
            r = fn(root.right)
            
            return 1 + max(l,r)

    LeetCode 104: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def md(root):
            if not root: return 0
            lft = md(root.left)
            ryt = md(root.right)
            
            return 1+max(lft, ryt)
        
        return md(root)
      
      
