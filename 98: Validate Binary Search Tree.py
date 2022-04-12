"""
  Approaches:
        
        1. Using Inorder Travarsal: TC: O(N)   SC: O(N) for storing array OR O(1) for storing only previous root.val
                
                a. Take 2 lis vars: res = [True] and inord = [-inf]
                b. Do the inorder trav and check..... if inord[0] >= root.val: if yes res[0] = False
                c. each time store last ele ie, inord[0] = root.val
                return res[0]
        
        2. Giving Range to each node: TC: O(N)    SC: O(1):
        
                Intution: We will provide each node with the range and if its not in range return false
                          range will be like 
                          for root => [-inf, inf], root.left => [-inf, root.val], root.right => [root.val, inf]
                
                a. mn mx = -inf, inf
                b. pass in func along with root
                c. if not root: return True
                d. if root.val <= mn or root.val >= mx: return False
                e. return func(root.left, mn, root.val) and func(root.right, root.val, mx)
                
     LeetCode 98: https://leetcode.com/problems/validate-binary-search-tree/
     YT: https://www.youtube.com/watch?v=f-sj7I5oXEI
"""

#### Range Method ########
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(root, mn, mx):
            if not root: return True
            if root.val <= mn or root.val >= mx:return False
            return check(root.left, mn, root.val) and check(root.right, root.val, mx)
        
        mn, mx = -inf, inf
        return check(root, mn, mx)


###### Store Ele method ######
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root: return 
            check(root.left)
            
            if inord[0] >= root.val: res[0] = False    
            inord[0] = root.val
            
            check(root.right)
            
        res = [True]
        inord = [-inf]
        
        check(root)
        return res[0]


