"""
   Approaches: 
        
        1. Using Inorder array: TC: O(1) for next and Hasnext    SC: O(N) for inorder array
            
            a. In constructor, Have inorder array, pointer = 0, ln = len(inorder)
            b. each time next is called print the inorder[pointer] and update pointer
            c. for hasNext return p == ln
            
        2. Storing nodes in Stack "Inorder":   TC: Average O(1) for next, O(1) for hasNext   **SC: O(H)
            
            a. in Constructor, have a stack 
            b. Store left nodes into Stack   
            c. on call for next: pop from stack
            d. if popped node has right than store that right in stack than all left nodes and return popped node data
            e. For hasNext return stack != []
            
        LeetCode 173: https://leetcode.com/problems/binary-search-tree-iterator/
        YT: https://www.youtube.com/watch?v=D2jMcmxU4bs
"""
############ FOR O(H) ##########
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.fillStack(root)
        

    def fillStack(self, root):
        self.st.append(root)
        while root.left:
            self.st.append(root.left)    
            root = root.left
            
    def next(self) -> int:
        pointer = self.st.pop()
        if pointer.right: self.fillStack(pointer.right)
        return pointer.val
        

    def hasNext(self) -> bool:
        return self.st != []


