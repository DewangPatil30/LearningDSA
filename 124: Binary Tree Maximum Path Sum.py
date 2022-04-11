"""
 Approach: 
    
        Intution: 
            a. PathSum on particular node is (node.val + leftPathSum + rightPathSum)
            b. So we will use the maxHight of BT formula and on place of 1 + max(l, r) 
            c. We will take node.val + max(l, r)
            d. also we wont take any -ve path sum ie, leftSum = max(0, postOrd(root.left)) same for rightSum
            e. We will maintain maxSum[0] = max(maxSum[0], node.val + l + r)
       
       LeetCode 124: https://leetcode.com/problems/binary-tree-maximum-path-sum/
       YT: https://www.youtube.com/watch?v=WszrfSwMz58
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def p(root):
            
            if not root: return 0
            
            l = max(0, p(root.left))
            r = max(0, p(root.right))
            
            sumPath = root.val + l + r
            
            res[0] = max(res[0], sumPath)
            
            return root.val + max(l, r)
        
        
        if not root: return 0
        if not (root.left or root.right): return root.val
        

        res = [-999999]
        p(root)
        return res[0]
    
    
