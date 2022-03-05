"""
LeetCode 98: https://leetcode.com/problems/validate-binary-search-tree/
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def check(root, mn, mx):
            
            if not root: return True
            
            if root.val <= mn or root.val >= mx:
                return False
            
            return check(root.left, mn, root.val) and check(root.right, root.val, mx)
                
            
            
        if not root.left and not root.right: return True
        mn, mx = -inf, inf
        return check(root, mn, mx)
            
