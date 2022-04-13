"""
Explaination: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
  
  READ MAIN SOLUTION THAN SOLUTION IN COMMENTS RETURN BY: GabrielD-
  tc: O(N^2) sc: O(N)

"""
class Codec:

    def serialize(self, root):
        if not root: return 'x'
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
    def generate(self):
        if self.data[0] == 'x': 
            self.data.pop(0)
            return
        
        root = TreeNode(int(self.data.pop(0)))
        root.left = self.generate()
        root.right = self.generate()
        
        return root
    
    def deserialize(self, data):
        self.data = data.split()
        root = self.generate()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
