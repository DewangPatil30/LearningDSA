"""
Approach: 
        
        If abs diff b/w leftHeight and rightHeight > 1: Res[0] = False
        check while computing max height 
        
    LeetCode 110: https://leetcode.com/problems/balanced-binary-tree/
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def fn(root):
            
            if not root: return 0
            l = fn(root.left)
            r = fn(root.right)
            
            if abs(l-r) > 1: res[0] = False
                
            return 1 + max(l,r)    
            
        
        res = [True]
        fn(root)
        return res[0]

                









