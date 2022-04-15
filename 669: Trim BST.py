"""
Approach:   When {node.val > high}node.val > high, we know that the trimmed binary tree must occur to the left of the node. 
            Similarly, when {node.val < low}node.val < low, 
            the trimmed binary tree occurs to the right of the node. 
            Otherwise, we will trim both sides of the tree.
        
        1: Using Recursion in BST: TC: O(N)   AUX SC: O(N)
        
            a. Make a func trim and pass the root, h, low
            b. if root.val > high: return trim(root.left)
            c. if root.val < low: return trim(root.right)
            d. root.left = trim(root.left)
               root.right = trim(root.right)

               return root
            return trim(root)
        
LeetCode 669: https://leetcode.com/problems/trim-a-binary-search-tree/
"""

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
        
        
