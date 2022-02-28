class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            
        nroot = root
        
        def invert(root):    
            if not root: return root

            root.left, root.right = root.right, root.left

            invert(root.left)
            invert(root.right)
            
        invert(root)
        return nroot
      
      
