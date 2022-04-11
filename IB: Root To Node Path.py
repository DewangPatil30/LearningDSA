"""
Approach: 

    1. Inorder Travasal: O(N) O(N) Aux
        
        a. Take arr and pass with function (In python not needed to pass)
        b. if not root: return False
        c. arr.append(root.val) than check if root.val == target: return True
        d. if trav(root.left, t) or trav(root.right, t): return True
        e. Else arr.pop() last inserted node
        return False
        
     IB: https://www.interviewbit.com/problems/path-to-given-node/
     YT: https://www.youtube.com/watch?v=fmflMqVOC7k      
"""

def solve(self, A, B):

        def trav(root, t):
            if not root: return False

            arr.append(root.val)
            if root.val == t: return True

            if trav(root.left, t) or trav(root.right, t):
                return True

            arr.pop()
            return False

        arr = []
        trav(A, B)
        return arr
    
    
