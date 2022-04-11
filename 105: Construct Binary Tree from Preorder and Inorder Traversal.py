"""
Approach: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        
        3                          3                          .  3 .
    [9]    [15, 20, 7]  ----> 9         20                 9       . 20 .
                                    [15]    [7]  ---->          15        7
        
    Take root val from preorder
    and root.left = recursive(l, index of root.val-1)
        root.right = recursive(index of root.val+1, r)
        
        return root

    LeetCode 105: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    YT Strivers: https://youtu.be/aZNaLrVebKQ
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        m = {k: i for i, k in enumerate(inorder)}
        preStack = preorder.copy()
        
        def constructTree(l, r):
            
            if l > r:
                return 
            
            root = TreeNode(preStack.pop(0))
            mid = root.val
            
            root.left = constructTree(l, m[mid]-1)
            root.right = constructTree(m[mid]+1, r)
            
            return root
        
        
        return constructTree(0, len(preorder)-1)
        
        
        
