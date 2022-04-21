"""
  Approaches:
            
            Slight Changes in max path sum in binary tree program
"""

class Solution:        
    def maxPathSum(self, root):
        
        def maxsum(root):
            if not root: return 0
            
            ls = maxsum(root.left)
            rs = maxsum(root.right)
            
            if root.left and root.right:
                res[0] = max(res[0], root.data + ls + rs)
                return root.data + max(ls, rs)
                
            if root.left: return ls + root.data
            else: return rs + root.data
            
            return root.data + max(ls, rs)
            
            
        res = [-inf]
        ans = maxsum(root)
        
        if not root.left or not root.right:
            res[0] = max(res[0], ans)
            
        return res[0]
    
    
