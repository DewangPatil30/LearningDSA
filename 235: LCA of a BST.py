"""
   Approach: Same as LCA of BT but here we have an advantage that left is smaller than root which is smaller than right
        
        a. Take p as node with greater value and q as the smaller val node
        b. If not root or root.val <= p.val and root.val >= q.val:
                return root
                
        c. left = right = None
        d. if root.val < p.val:
               left = search(root.left)
           if root.val > p.val:
               right = search(root.right)
               
        e. if not left: return right
           if not right: return left
           return root
       
    LeetCode 235: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val < q.val:       #For p must be greater than q
            return self.lowestCommonAncestor(root, q, p)
        
        if not root or root.val <= p.val and root.val >= q.val:
            return root
        
        left = right = None
        
        if root.val > p.val:
            left = self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left: return right
        if not right: return left
        return root
            
        
