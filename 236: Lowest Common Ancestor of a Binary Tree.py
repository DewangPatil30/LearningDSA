"""
Approaches: 
        
        1. Brute Force: TC: O(N)    SC: O(N):
            
            a. Find the root to node path of first node p and store in array
            b. Find the root to node path of second path q and store in another array
            c. Loop for min len b/w parray and qarray
            d. Return the last same node as ans
            Note: if no return in the loop than: return qarray[-1] if len(parray) > len(qarray) else parray[-1]
            
     LeetCode 236: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
     YT: https://www.youtube.com/watch?v=_-QHfMDde90
"""
# BRUTE FORCEEEEEEE

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def path(root, t):
            if not root: return False
            
            arr.append(root)
            
            if root == t: return True
            if path(root.left, t) or path(root.right, t): return True
            
            arr.pop()
            return False
        
        arr = []
        path(root, p)
        forp = arr.copy()
        arr = []
        path(root, q)

        for i in range(min(len(arr), len(forp))):
            if forp[i] != arr[i]: return forp[i-1]
            
        if len(forp) > len(arr):
            return arr[-1]
        return forp[-1]
            
