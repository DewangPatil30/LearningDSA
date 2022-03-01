class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        
        def subchk(root, subroot):
            if not root and not subroot: return True
            elif not root or not subroot: return False
            
            if root.val == subroot.val:
                if subchk(root.left, subroot.left) and subchk(root.right, subroot.right):
                    return True

                
        def valchk(root, subroot):
            if not root: return
            
            if root.val == subroot.val and subchk(root, subroot): res[0] = True
                        
            if root.left: valchk(root.left, subroot)
            if root.right: valchk(root.right, subroot)
        
        res = [False]
        valchk(root, subroot) 
        return res[0]
      
      
