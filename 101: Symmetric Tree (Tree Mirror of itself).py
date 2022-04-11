"""
Approach: 
    
    Same as isSameTree concept:
    a. Just pass root.left as p and root.right as q
    b. In fn check if p.val == q.val and fn(p.left, q.right) and fn(p.right, q.left)
        If all true than return True
        else False
        
    LeetCode 101: https://leetcode.com/problems/symmetric-tree/
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetric(p, q):
            if not p and not q: return True
            if not p or not q: return False
            
            if p.val == q.val and symmetric(p.left, q.right) and symmetric(p.right, q.left):
                return True
            
            return False
        
        
        return symmetric(root.left, root.right)
      
      
